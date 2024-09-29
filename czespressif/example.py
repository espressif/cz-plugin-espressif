from __future__ import annotations

from czespressif.config import CommitType

# ANSI escape codes for colors and bold text
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
LIGHT_BLUE = '\033[96m'
PURPLE = '\033[35m'
BLUE = '\033[94m'
RESET = '\033[0m'


def build_example(types: list[CommitType], extra_types: list[CommitType]) -> str:
    """
    'cz example' command output.
    Generate an example guide for commit message schema and conventions.
    # Exclude 'BREAKING CHANGE' from the known types list
    """

    # Exclude 'BREAKING CHANGE' from the known types list
    filtered_types = [t for t in types if t.type != 'BREAKING CHANGE']

    # Format the known types section with two spaces of indentation
    types_formatted = '\n'.join(f'  {GREEN}{t.type}{RESET}: {t.description}' for t in filtered_types)
    extra_types_formatted = '\n'.join(f'  {BLUE}{t.type}{RESET}: {t.description}' for t in extra_types)
    if extra_types_formatted:
        extra_types_formatted += f'  {BLUE}<--- non standard type added by extra_types{RESET}'

    # Example guide with colors and bold text
    example_guide = f"""
---

{BOLD}{YELLOW}Commit message schema:{RESET}

    {YELLOW}<type>(<scope>): <subject>{RESET}
        <... empty line ...>
    {YELLOW}<body>{RESET}
        <... empty line ...>
    {YELLOW}(BREAKING CHANGE: <breaking changes>)*{RESET}
    {YELLOW}(<footers>)*{RESET}

---

{BOLD}{GREEN}Commit types in this project:{RESET}

{types_formatted}
{extra_types_formatted}

---

{BOLD}{LIGHT_BLUE}Short commit messages (one line):{RESET}

    {LIGHT_BLUE}fix{RESET}: fix something (present or imperative, no period)
    {LIGHT_BLUE}fix(package){RESET}: fix something
    {LIGHT_BLUE}feat(name){RESET}: add a new feature
    {LIGHT_BLUE}refactor(package){RED}!{RESET}: this refactoring {RED}breaks the thing{RESET}

---

{BOLD}{BLUE}Full commit messages with body and footer:{RESET}

    {BLUE}feat(something){RESET}: add something new (present/imperative, no period)

    Here optionally comes the details - this is commit message body.
    It can be multiline, hyphens, asterisks, are okay.

    {RED}BREAKING CHANGE: It breaks something!{RESET}
    {BLUE}Closes https://github.com/espressif/<project>/issues/<issue_number>{RESET}

---

{BOLD}{PURPLE}More info:{RESET}

- https://www.conventionalcommits.org/en/v1.0.0/#specification
- https://github.com/{PURPLE}espressif/conventional-precommit-linter{RESET}
- https://github.com/{PURPLE}espressif/standards{RESET}
    """

    return example_guide


def build_info() -> str:
    """
    'cz info' command output.
    Returns information about a custom Commitizen plugin for Espressif Systems.
    """
    return (
        'This is a custom Commitizen plugin for Espressif Systems. \n'
        'It is mainly used to generate consistent and beautiful changelog with minimum settings from target project. \n'
        'Can be used for creating commit messages, that passes Espressif standards. \n'
        'Customization from target project is possible, check this plugin GitHub repo'
    )
