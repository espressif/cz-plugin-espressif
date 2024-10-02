from __future__ import annotations

from datetime import datetime
from typing import Literal

TYPES: list[dict] = [  # this is order in changelog
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
        'type': 'docs',
        'description': 'Documentation only change',
        'heading': 'Documentation',
        'emoji': '📖',
        'bump': 'PATCH',
        'changelog': True,
    },
    {
        'type': 'refactor',
        'description': 'A changeset neither fixing a bug nor adding a feature',
        'heading': 'Code refactoring',
        'emoji': '🔧',
        'bump': 'PATCH',
        'changelog': True,
    },
    {
        'type': 'remove',
        'description': 'Removing code or files',
        'heading': 'Removals',
        'emoji': '🗑️',
        'bump': 'PATCH',
        'changelog': True,
    },
    {
        'type': 'change',
        'description': 'A change made to the codebase.',
        'heading': 'Changes',
        'emoji': '🏗️',
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
        'type': 'test',
        'description': 'Adding missing or correcting existing tests',
        'heading': 'Testing',
        'emoji': '🚦',
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
]

CHANGELOG_TITLE: str = """
<a href="https://www.espressif.com">
    <img src="czespressif/templates/espressif-logo.svg" align="right" height="20" />
</a>

# CHANGELOG
"""

CHANGELOG_HEADER: str = """
> All notable changes to this project are documented in this file.
> This list is not exhaustive - only important changes, fixes, and new features in the code are reflected here.

<div align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/Keep%20a%20Changelog-v1.1.0-salmon?logo=keepachangelog&logoColor=black&labelColor=white&link=https%3A%2F%2Fkeepachangelog.com%2Fen%2F1.1.0%2F">
    <img alt="Static Badge" src="https://img.shields.io/badge/Conventional%20Commits-v1.0.0-pink?logo=conventionalcommits&logoColor=black&labelColor=white&link=https%3A%2F%2Fwww.conventionalcommits.org%2Fen%2Fv1.0.0%2F">
    <img alt="Static Badge" src="https://img.shields.io/badge/Semantic%20Versioning-v2.0.0-grey?logo=semanticrelease&logoColor=black&labelColor=white&link=https%3A%2F%2Fsemver.org%2Fspec%2Fv2.0.0.html">
</div>
<hr>
"""

CHANGELOG_FOOTER: str = f"""
<div align="center">
    <small>
        <b>
            <a href="https://www.github.com/espressif/cz-plugin-espressif">Commitizen Espressif plugin</a>
            ·
            <a href="https://www.github.com/espressif/standards">Espressif Standards</a>
        </b>
    <br>
        <sup><a href="https://www.espressif.com">Espressif Systems CO LTD. ({datetime.now().year})</a><sup>
    </small>
</div>
"""

INCREMENT = Literal['MAJOR', 'MINOR', 'PATCH']

# Currently BUMP_MESSAGE not possible to define default here - if not provided from pyproject.toml, it will be commitizen default, not ours :(
BUMP_MESSAGE: str = 'change(bump): release $current_version → $new_version [skip-ci]'

ESCAPE_MARKDOWN_SEQ: list[str] = [r'_{', r'}_']
