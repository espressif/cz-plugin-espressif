from __future__ import annotations

import re
import sys

from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from functools import cached_property
from functools import total_ordering
from typing import Dict
from typing import List
from typing import Literal
from typing import Union

from commitizen.config import read_cfg
from commitizen.defaults import Settings

from czespressif.defaults import CHANGELOG_FOOTER
from czespressif.defaults import CHANGELOG_HEADER
from czespressif.defaults import CHANGELOG_TITLE
from czespressif.defaults import TYPES

RE_HTTP = re.compile(r'(?P<server>https?://.+)/(?P<repository>[^/]+/[^/]+/?)')
INCREMENT = Literal['MAJOR', 'MINOR', 'PATCH']


@dataclass
@total_ordering
class CommitType:
    type: str  # Key used as type in the commit header.
    description: str  # A human-readable description of the type.
    heading: Union[str, None] = None  # The resulting heading in the changelog for this type.
    emoji: Union[str, None] = None  # An optional emoji representing the type.
    changelog: bool = True  # Whether this type should appear in the changelog or not.
    question: bool = True  # Whether this type should appear in the question choices.
    bump: Union[INCREMENT, None] = None  # Specifies the version bump category (e.g., 'MAJOR', 'MINOR', 'PATCH').
    regex: Union[str, None] = None  # An optional regular expression matching this type.

    def __str__(self) -> str:
        return self.type

    def __hash__(self):
        return hash(self.type)

    def __eq__(self, other) -> bool:
        return self._compare_key(other) == 0

    def __lt__(self, other) -> bool:
        return self._compare_key(other) < 0

    def _compare_key(self, other) -> int:
        """Helper method for comparing with either CommitType or str."""
        if isinstance(other, CommitType):
            other_type = other.type.lower()
        elif isinstance(other, str):
            other_type = other.lower()
        else:
            return NotImplemented
        return (self.type.lower() > other_type) - (self.type.lower() < other_type)

    @classmethod
    def from_dict(cls, data: Dict) -> CommitType:
        """Creates a CommitType instance from a dictionary."""
        valid_fields = {f.name for f in fields(cls)}
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}
        return cls(**filtered_data)

    @classmethod
    def from_list(cls, lst: List[Dict]) -> List[CommitType]:
        """Creates a list of CommitType instances from a list of dictionaries."""
        return [cls.from_dict(d) for d in lst]


class CzEspressifSettings(Settings):
    types: Union[list[dict], None]  # The list of accepted types
    extra_types: Union[list[dict], None]  # A list of additional types (permit addition without losing defaults)
    github: Union[str, None]
    gitlab: Union[str, None]
    jira_url: Union[str, None]
    jira_prefixes: Union[list[str], None]
    order_by_scope: Union[bool, None]
    group_by_scope: Union[bool, None]
    include_unreleased: Union[bool, None]
    use_emoji: Union[bool, None]
    changelog_title: Union[str, None]
    changelog_header: Union[str, None]
    changelog_footer: Union[str, None]


@dataclass
class CzEspressifConfig:
    settings: CzEspressifSettings = field(default_factory=lambda: read_cfg().settings)

    @property
    def types(self) -> list[CommitType]:
        return CommitType.from_list(self.settings.get('types', TYPES))

    @property
    def extra_types(self) -> list[CommitType]:
        return CommitType.from_list(self.settings.get('extra_types', []))

    @cached_property
    def known_types(self) -> list[CommitType]:
        return self.types + self.extra_types

    @cached_property
    def github(self) -> Union[str, None]:
        repository = self.settings.get('github')
        if not repository:
            return None
        match = RE_HTTP.match(repository)
        return match.group('repository') if match else repository

    @cached_property
    def github_url(self) -> str:
        repository = self.settings.get('github')
        if repository:
            match = RE_HTTP.match(repository)
            if match:
                return match.group('server')
        return 'https://github.com'

    @cached_property
    def gitlab(self) -> Union[str, None]:
        repository = self.settings.get('gitlab')
        if not repository:
            return None
        match = RE_HTTP.match(repository)
        return match.group('repository') if match else repository

    @cached_property
    def gitlab_url(self) -> str:
        repository = self.settings.get('gitlab')
        if repository:
            match = RE_HTTP.match(repository)
            if match:
                return match.group('server')
        return 'https://gitlab.com'

    @cached_property
    def jira_url(self) -> Union[str, None]:
        return self.settings.get('jira_url')

    @cached_property
    def jira_prefixes(self) -> list[str]:
        return self.settings.get('jira_prefixes', [])

    @property
    def incremental(self) -> bool:
        return '--incremental' in sys.argv

    @property
    def order_by_scope(self) -> bool:
        return self.settings.get('order_by_scope') or False

    @property
    def include_unreleased(self) -> bool:
        return self.settings.get('include_unreleased', True)

    @property
    def use_emoji(self) -> bool:
        return self.settings.get('use_emoji', True)

    @property
    def changelog_title(self) -> str:
        return self.settings.get('changelog_title', CHANGELOG_TITLE)

    @property
    def changelog_header(self) -> str:
        return self.settings.get('changelog_header', CHANGELOG_HEADER)

    @property
    def changelog_footer(self) -> str:
        return self.settings.get('changelog_footer', CHANGELOG_FOOTER)

    # @property
    # def bump_message(self) -> str:
    #     if not
