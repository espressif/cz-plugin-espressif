from __future__ import annotations

from typing import Dict
from typing import List

TYPES: List[Dict] = [
    {
        'type': 'BREAKING CHANGE',
        'description': 'Changes that are not backward-compatibles',
        'heading': 'Breaking changes',
        'emoji': '🚨',
        'bump': 'MAJOR',
        'regex': r'BREAKING[\-\ ]CHANGE',
        'question': False,  # Breaking changes have a dedicated question
        'changelog': True,
    },
    {
        'type': 'feat',
        'description': 'A new feature',
        'heading': 'New features',
        'emoji': '✨',
        'bump': 'MINOR',
        'changelog': True,
    },
    {
        'type': 'fix',
        'description': 'A bug fix',
        'heading': 'Bug fixes',
        'emoji': '🐛',
        'bump': 'PATCH',
        'changelog': True,
    },
    {
        'type': 'change',
        'description': 'A change made to the codebase.',
        'heading': 'Changes',
        'emoji': '🏗️',
        'bump': 'PATCH',
        'changelog': True,
    },
    {
        'type': 'docs',
        'description': 'Documentation only change',
        'heading': 'Documentation',
        'emoji': '📖',
        'bump': 'PATCH',
        'changelog': True,
    },
    {
        'type': 'test',
        'description': 'Adding missing or correcting existing tests',
        'heading': 'Testing',
        'emoji': '🚦',
        'bump': 'PATCH',
        'changelog': False,
    },
    {
        'type': 'ci',
        'description': 'Changes to CI configuration files and scripts',
        'heading': 'CI and project settings',
        'emoji': '⚙️',
        'bump': 'PATCH',
        'changelog': False,
    },
    {
        'type': 'refactor',
        'description': 'A changeset neither fixing a bug nor adding a feature',
        'heading': 'Refactoring',
        'emoji': '🔧',
        'bump': 'PATCH',
        'changelog': False,
    },
    {
        'type': 'revert',
        'description': 'Revert one or more commits',
        'heading': 'Reverted',
        'emoji': '🔙',
        'bump': 'PATCH',
        'changelog': False,
    },
    {
        'type': 'remove',
        'description': 'Removing code or files',
        'heading': 'Removals',
        'emoji': '🗑️',
        'bump': 'PATCH',
        'changelog': True,
    },
]

CHANGELOG_TITLE: str = 'Changelog'

CHANGELOG_HEADER: str = """
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---"""


CHANGELOG_FOOTER: str = """**Created by [Espressif Systems CO LTD.](https://www.espressif.com/)**
- [Commitizen tools plugin with Espressif code style](https://www.github.com/espressif/cz-plugin-espressif)
- [Espressif Coding Standards and Best Practices](https://www.github.com/espressif/standards)"""

# Currently not possible to define default here - if not provided from pyproject.toml, it will be commitizen default, not ours :(
BUMP_MESSAGE: str = 'change(bump): release $current_version → $new_version [skip-ci]'
