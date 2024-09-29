from __future__ import annotations

import re
import sys

from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from functools import cached_property
from functools import total_ordering
from typing import cast

from commitizen.config import read_cfg
from commitizen.defaults import Settings

from czespressif.defaults import CHANGELOG_FOOTER
from czespressif.defaults import CHANGELOG_HEADER
from czespressif.defaults import CHANGELOG_TITLE
from czespressif.defaults import INCREMENT
from czespressif.defaults import TYPES


@dataclass
@total_ordering
class CommitType:
    type: str  # Key used as type in the commit header.
    description: str  # A human-readable description of the type.
    heading: str | None = None  # The resulting heading in the changelog for this type.
    emoji: str | None = None  # An optional emoji representing the type.
    changelog: bool = True  # Whether this type should appear in the changelog or not.
    question: bool = True  # Whether this type should appear in the question choices.
    bump: INCREMENT | None = None  # Specifies the version bump category (e.g., 'MAJOR', 'MINOR', 'PATCH').
    regex: str | None = None  # An optional regular expression matching this type.

    def __str__(self) -> str:
        return self.type

    def __hash__(self) -> int:
        return hash(self.type)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, CommitType):
            return self._compare_key(other) == 0
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, CommitType):
            return self._compare_key(other) < 0
        return NotImplemented

    def _compare_key(self, other: object) -> int:
        """Helper method for comparing with either CommitType or str."""
        if isinstance(other, CommitType):
            other_type = other.type.lower()
        elif isinstance(other, str):
            other_type = other.lower()
        else:
            return NotImplemented
        return (self.type.lower() > other_type) - (self.type.lower() < other_type)

    @classmethod
    def from_dict(cls, data: dict) -> CommitType:
        """Creates a CommitType instance from a dictionary."""
        valid_fields = {f.name for f in fields(cls)}
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}
        return cls(**filtered_data)

    @classmethod
    def from_list(cls, lst: list[dict]) -> list[CommitType]:
        """Creates a list of CommitType instances from a list of dictionaries."""
        return [cls.from_dict(d) for d in lst]


class CzEspressifSettings(Settings):
    types: list[dict] | None
    extra_types: list[dict] | None
    changelog_unreleased: bool | None
    use_emoji: bool | None
    changelog_title: str | None
    changelog_header: str | None
    changelog_footer: str | None
    changelog_section_line: bool | None
    changelog_show_commits: bool | None
    changelog_show_authors: bool | None
    release_notes_footer: str | None


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

    @property
    def incremental(self) -> bool:
        cli_version = any(re.match(r'^v?\d+\.\d+\.\d+$', arg) for arg in sys.argv)  # re: '(v)MAJOR.MINOR.PATCH'
        cli_version_range = any(re.match(r'^v?\d+\.\d+\.\d+\.\.v?\d+\.\d+\.\d+$', arg) for arg in sys.argv)  # re: '(v)MAJOR.MINOR.PATCH..(v)MAJOR.MINOR.PATCH'
        cli_incremental_flag = '--incremental' in sys.argv
        cli_bump = 'bump' in sys.argv

        is_incremental = any([cli_version, cli_version_range, cli_incremental_flag, cli_bump])
        return cast(bool, self.settings.get('incremental', is_incremental))

    @property
    def changelog_unreleased(self) -> bool:
        return cast(bool, self.settings.get('changelog_unreleased', True))

    @property
    def use_emoji(self) -> bool:
        return cast(bool, self.settings.get('use_emoji', True))

    @property
    def changelog_title(self) -> str:
        return cast(str, self.settings.get('changelog_title', CHANGELOG_TITLE))

    @property
    def changelog_header(self) -> str:
        return cast(str, self.settings.get('changelog_header', CHANGELOG_HEADER))

    @property
    def changelog_footer(self) -> str:
        return cast(str, self.settings.get('changelog_footer', CHANGELOG_FOOTER))

    @property
    def changelog_section_line(self) -> bool:
        return cast(bool, self.settings.get('changelog_section_line', True))

    @property
    def changelog_show_commits(self) -> bool:
        return cast(bool, self.settings.get('changelog_show_commits', True))

    @property
    def changelog_show_authors(self) -> bool:
        return cast(bool, self.settings.get('changelog_show_authors', True))

    @property
    def release_notes_footer(self) -> str:
        return cast(str, self.settings.get('release_notes_footer', ''))
