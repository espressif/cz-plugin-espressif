from __future__ import annotations

from dataclasses import dataclass
from random import getrandbits

import pytest

from commitizen.config import BaseConfig
from commitizen.git import GitCommit
from syrupy.extensions.single_file import SingleFileSnapshotExtension
from syrupy.extensions.single_file import WriteMode

from czespressif.config import CzEspressifConfig
from czespressif.config import CzEspressifSettings


class MarkdownSnapshotExtension(SingleFileSnapshotExtension):
    _file_extension = 'md'
    _write_mode = WriteMode.TEXT


@pytest.fixture
def snapshot(snapshot):
    return snapshot.use_extension(MarkdownSnapshotExtension)


def randbytes(size: int) -> bytes:
    return bytearray(getrandbits(8) for _ in range(size))


@dataclass
class Factory:
    config: CzEspressifConfig

    def parsed_message(self, **kwargs) -> tuple[dict, GitCommit]:
        parsed = {'type': 'change', 'scope': None, 'message': 'I am a message', **kwargs}
        prefix = parsed['type']
        msg = [f'{prefix}: {parsed["message"]}']
        body = parsed.get('body')
        if body is not None:
            msg.extend(('', body))
        footer = parsed.get('footer')
        if footer is not None:
            msg.extend(('', footer))
        return parsed, self.commit('\n'.join(msg))

    def commit(self, title: str, **kwargs) -> GitCommit:
        return GitCommit(rev=str(randbytes(8)), title=title, **kwargs)


@pytest.fixture
def settings(request) -> CzEspressifSettings:
    settings = CzEspressifSettings()
    for marker in reversed(list(request.node.iter_markers('settings'))):
        settings.update(marker.kwargs)
    return settings


@pytest.fixture
def config(settings):
    config = BaseConfig()
    config.settings.update({'name': 'czespressif'})
    config.settings.update(settings)
    return config


@pytest.fixture
def cze_config(settings) -> CzEspressifConfig:
    return CzEspressifConfig(settings)


@pytest.fixture
def factory(cze_config: CzEspressifConfig) -> Factory:
    return Factory(cze_config)
