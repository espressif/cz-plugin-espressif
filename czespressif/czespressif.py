from __future__ import annotations

import itertools
import re

from collections import OrderedDict
from collections.abc import Iterable
from typing import Any

from commitizen.cz.base import BaseCommitizen
from commitizen.cz.base import BaseConfig
from commitizen.defaults import Questions
from jinja2 import PackageLoader

from czespressif.config import CommitType
from czespressif.config import CzEspressifConfig
from czespressif.defaults import ESCAPE_MARKDOWN_SEQ
from czespressif.defaults import INCREMENT
from czespressif.example import build_example
from czespressif.example import build_info
from czespressif.questions import get_questions


class CzPluginEspressif(BaseCommitizen):  # pylint: disable=abstract-method
    template_loader = PackageLoader('czespressif', 'templates')

    def __init__(self, config: BaseConfig):
        super().__init__(config)
        self.cze_config = CzEspressifConfig(config.settings)

    @property
    def known_types(self) -> dict[str, CommitType]:
        return dict(itertools.chain((t.type, t) for t in self.cze_config.known_types))

    @property
    def re_known_types(self) -> str:
        return '|'.join(t.regex or k for k, t in self.known_types.items())

    @property
    def changelog_pattern(self) -> str:
        re_known_types = '|'.join(k for k, t in self.known_types.items())
        return rf'\A({re_known_types})(\(.+\))?(!)?'

    @property
    def change_type_map(self) -> dict[str, str]:
        return dict(
            itertools.chain(
                ((t.type, f'{t.emoji + " " if self.cze_config.use_emoji and t.emoji else ""}{t.heading}') for t in self.cze_config.known_types if t.heading),
            )
        )

    @property
    def change_type_order(self) -> list[str]:
        return [
            f'{commit_type.emoji} {commit_type.heading}' if self.cze_config.use_emoji and commit_type.emoji else commit_type.heading
            for commit_type in self.cze_config.known_types
            if commit_type.changelog and commit_type.heading
        ]

    @property
    def bump_pattern(self) -> str:
        """Regex to extract information from commit (subject and body)"""
        re_types = '|'.join(t.regex or k for k, t in self.known_types.items() if t.bump)
        return rf'^((({re_types})(\(.+\))?(!)?)|\w+!):'

    @property
    def bump_map(self) -> dict[str, INCREMENT]:
        """
        Mapping the extracted information to a SemVer increment type (MAJOR, MINOR, PATCH)
        """
        return OrderedDict(
            (
                (r'^.+!$', 'MAJOR'),
                *((rf'^{t.regex or k}', t.bump) for k, t in self.known_types.items() if t.bump),
            )
        )

    @property
    def bump_map_major_version_zero(self) -> dict[str, INCREMENT]:
        return OrderedDict((pattern, increment.replace('MAJOR', 'MINOR')) for pattern, increment in self.bump_map.items())  # type: ignore

    @property
    def commit_parser(self) -> str:
        return (
            rf'(?P<change_type>{self.re_known_types})'
            r'(?:\((?P<scope>[^()\r\n]*)\))?'  # Optional scope
            r'(?P<breaking>!)?:\s'
            r'(?P<message>.*)'  # Required message
            r'(?:\n{2,}(?P<body>.*))?'  # Optional body
            r'(?:\n{2,}(?P<footer>.*))?'  # Optional footer
        )

    @property
    def template_extras(self) -> dict[str, Any]:
        return {'config': self.cze_config, 'settings': self.cze_config.settings}

    def questions(self) -> Questions:
        return get_questions(self.cze_config)

    def message(self, answers: dict[str, Any]) -> str:
        prefix = answers['type']
        scope = answers['scope']
        subject = answers['subject']
        body = answers['body']
        is_breaking_change = answers['is_breaking_change']
        breaking_change = answers.get('breaking_change')
        footer = answers.get('footer', '')
        extra = ''

        if scope:
            scope = f'({scope})'

        if is_breaking_change and not breaking_change:
            scope += '!'

        if body:
            body = f'\n\n{body}'

        if is_breaking_change and breaking_change:
            footer = f'BREAKING CHANGE: {breaking_change}\n{footer}'

        if footer:
            footer = f'\n\n{footer}'

        message = f'{prefix}{scope}: {subject}{extra}{body}{footer}'

        return message

    def wrap_problematic_parts(self, message: str) -> str:
        """Escape problematic underscores near curly braces without altering other underscores."""
        # Dynamically build regex pattern to handle all known issues
        for issue in ESCAPE_MARKDOWN_SEQ:
            # For each known issue, replace underscores with escaped underscores
            message = re.sub(issue, lambda match: match.group(0).replace('_', r'\_'), message)
        return message

    def changelog_message_builder_hook(self, parsed_message: dict[str, Any], commit: Any) -> dict[str, Any] | Iterable[dict[str, Any]] | None:  # pylint: disable=unused-argument
        # Remap breaking changes type
        if parsed_message.get('breaking'):
            parsed_message['change_type'] = 'BREAKING CHANGE'

        # Get the full list of types to include from pyproject.toml
        included_in_changelog = self.cze_config.settings.get('types_in_changelog', [])

        # If the list is empty (i.e., not set), include all default types
        if not included_in_changelog:
            commit_type = self.known_types.get(parsed_message['change_type'])
            if commit_type and commit_type.changelog:
                # Apply the escaping to the parsed message
                parsed_message['message'] = self.wrap_problematic_parts(parsed_message['message'])
                return parsed_message
            return None

        # Filter out all commit types not explicitly included in `types_in_changelog`
        if parsed_message['change_type'] not in included_in_changelog:
            return None

        # Apply the escaping to the parsed message
        parsed_message['message'] = self.wrap_problematic_parts(parsed_message['message'])

        return parsed_message

    def changelog_hook(self, full: str, partial: str | None) -> str:
        """Process resulting changelog to keep 1 empty line at the end of the file."""
        changelog = partial or full
        return changelog.rstrip() + '\n'

    def example(self) -> str:
        examples = build_example(types=self.cze_config.types, extra_types=self.cze_config.extra_types)
        return examples

    def schema(self) -> str:
        return '<type>(<scope>): <subject>\n' '<BLANK LINE>\n' '<body>\n' '<BLANK LINE>\n' '(BREAKING CHANGE: <breaking changes>)*\n' '(<footers>)*'

    def schema_pattern(self) -> str:
        pattern = (
            r'(?s)'  # To explicitly make . match new line
            rf'({self.re_known_types})'  # type
            r'(\(\S+\))?!?:'  # scope
            r'( [^\n\r]+)'  # subject
            r'((\n\n.*)|(\s*))?$'
        )
        return pattern

    def info(self) -> str:
        return build_info()


discover_this = CzPluginEspressif  # pylint: disable=invalid-name
