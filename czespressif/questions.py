from __future__ import annotations

from typing import Any

from commitizen.cz import exceptions

from czespressif.config import CzEspressifConfig


def required_validator(answer: str, msg: str = '') -> str:
    if not answer:
        raise exceptions.AnswerRequiredError(msg)
    return answer


def multiple_line_breaker(answer: str, sep: str = '|') -> str:
    return '\n'.join(line.strip() for line in answer.split(sep) if line)


def parse_scope(text: str) -> str:
    if not text:
        return ''
    scope = text.strip().split()
    if len(scope) == 1:
        return scope[0]
    return '-'.join(scope)


def parse_subject(text: str) -> str:
    if isinstance(text, str):
        text = text.strip('.').strip()
    return required_validator(text, msg='Subject is required.')


def get_questions(cze_config: CzEspressifConfig) -> list[dict[str, Any]]:
    """Questions regarding the commit message."""

    type_padding = 10  # Define the padding for the type part
    description_column = 25  # Define where the description should start
    extra_space_emoji = ['change', 'ci', 'remove']  # Types that need extra space behind the emoji

    return [
        {
            'type': 'list',
            'name': 'type',
            'message': 'Select the type of change you are committing',
            'choices': [
                {
                    'value': t.type,
                    # Add an extra space behind the emoji for specific types
                    'name': f'{t.type:<{type_padding}}'
                    + ' ' * (description_column - len(f'{t.type:<{type_padding}}'))
                    + f'{t.emoji}{"  " if t.type in extra_space_emoji else " "} {t.description}',
                }
                for t in cze_config.known_types
                if t.question
            ],
        },
        {
            'type': 'input',
            'name': 'scope',
            'message': 'Scope. Define Could be anything specifying place of the commit change (wifi, bt, core):\n',
            'filter': parse_scope,
        },
        {
            'type': 'input',
            'name': 'subject',
            'filter': parse_subject,
            'message': 'Subject. Concise description of the changes. Imperative, lower case and no period:\n',
        },
        {
            'type': 'input',
            'name': 'body',
            'message': 'Provide additional contextual information - commit message BODY: (press [enter] to skip)\n',
            'filter': multiple_line_breaker,
        },
        {
            'type': 'confirm',
            'name': 'is_breaking_change',
            'message': 'Is this a BREAKING CHANGE?\n',
            'default': False,
        },
        {
            'when': lambda x: x['is_breaking_change'],
            'type': 'input',
            'name': 'breaking_change',
            'message': 'Breaking changes. Details the breakage:\n',
            'filter': multiple_line_breaker,
        },
        {
            'type': 'input',
            'name': 'footer',
            'message': 'Footer. Information about Breaking Changes and reference issues that this commit impacts: (press [enter] to skip)\n',
            'filter': multiple_line_breaker,
        },
    ]
