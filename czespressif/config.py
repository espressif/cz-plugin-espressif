from __future__ import annotations

import sys

from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from functools import cached_property
from functools import total_ordering
from typing import Dict
from typing import List
from typing import Union

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
    types: Union[list[dict], None]
    extra_types: Union[list[dict], None]
    changelog_unreleased: Union[bool, None]
    use_emoji: Union[bool, None]
    changelog_title: Union[str, None]
    changelog_header: Union[str, None]
    changelog_footer: Union[str, None]
    changelog_section_line: Union[bool, None]
    changelog_show_commits: Union[bool, None]
    changelog_show_authors: Union[bool, None]


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
        return '--incremental' in sys.argv

    @property
    def changelog_unreleased(self) -> bool:
        return self.settings.get('changelog_unreleased', True)

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

    @property
    def changelog_section_line(self) -> bool:
        return self.settings.get('changelog_section_line', True)

    @property
    def changelog_show_commits(self) -> bool:
        return self.settings.get('changelog_show_commits', True)

    @property
    def changelog_show_authors(self) -> bool:
        return self.settings.get('changelog_show_authors', True)
