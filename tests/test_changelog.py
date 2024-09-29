from __future__ import annotations

from pathlib import Path

import pytest

from commitizen import git
from commitizen.changelog import Metadata
from commitizen.commands.changelog import Changelog
from commitizen.exceptions import DryRunExit
from pytest_mock import MockerFixture
from syrupy.extensions.single_file import SingleFileSnapshotExtension
from syrupy.extensions.single_file import WriteMode

FIXTURES = Path(__file__).parent / 'fixtures/changelogs'


class MarkdownSnapshotExtension(SingleFileSnapshotExtension):
    _file_extension = 'md'
    _write_mode = WriteMode.TEXT


@pytest.fixture
def snapshot(snapshot):
    return snapshot.use_extension(MarkdownSnapshotExtension)


COMMITS_DATA = [
    {
        'rev': '22c4820bd927ad017649bcf6e8d03e30ddc946e9',
        'title': 'change(bump): [skip-ci] release v1.2.0 → v1.3.0',
        'body': '',
        'author': 'Jane Hunter',
        'author_email': 'jane.hunter@espressif.com',
    },
    {
        'rev': 'b5e7a2d4c9f547d8b5c7f2a9e7c5d4a8e2d6b7c4',
        'title': 'feat(api): rollback changes to JWT token handling',
        'body': '',
        'author': 'Alice Johnson',
        'author_email': 'alice.johnson@espressif.com',
    },
    {
        'rev': 'd9b2c7e8f4b946a7f5c7a5b8d7f3e4c2b5a6f9d3',
        'title': 'fix(logging): switch from console logs to structured JSON logging',
        'body': '',
        'author': 'Eve Martin',
        'author_email': 'eve.martin@espressif.com',
    },
    {
        'rev': 'f2e7d1b7c4b942a5a5d3c2f9a7f5b4d9e5c3b7e4',
        'title': 'test(api): write unit tests for new password reset feature',
        'body': '',
        'author': 'Eve Martin',
        'author_email': 'eve.martin@espressif.com',
    },
    {
        'rev': 'b7a4c5b2d5e147c8b5f7a2e5d4c9e3b2a7f4d9e5',
        'title': 'fix: correct typos in error messages displayed on UI',
        'body': '',
        'author': 'Bob Smith',
        'author_email': 'bob.smith@espressif.com',
    },
    {
        'rev': 'c5d3e7a2f2b945c7a5e7d2b9f5c4e3b8d7f9e2a4',
        'title': 'feat(ui): improve loading animations for dashboard page',
        'body': '',
        'author': 'Diana White',
        'author_email': 'diana.white@espressif.com',
    },
    {
        'rev': 'e2d9a7f5b5e24c5f9b7d4f2c5a7e9b4c3d5e6f2a',
        'title': 'ci: add automated deployment script for production',
        'body': '',
        'author': 'Charlie Green',
        'author_email': 'charlie.green@espressif.com',
    },
    {
        'rev': 'd25d90e96d5f6bdeeca1f340cce9f7b87f7c8c0e',
        'title': 'change(bump): [skip-ci] release v1.2.0.rc0 → v1.2.0',
        'body': '',
        'author': 'Jane Hunter',
        'author_email': 'jane.hunter@espressif.com',
    },
    {
        'rev': 'd7e2f9b5c4b24b5a9a7b3d2f5c4e7f9c2b8e5d1f',
        'title': 'ci: configure linter to enforce new coding standards',
        'body': '',
        'author': 'Diana White',
        'author_email': 'diana.white@espressif.com',
    },
    {
        'rev': 'f5c7b1e4e4b947d9a7b5f2c5e4f9d7a8b5c3e7d9',
        'title': 'change(bump): [skip-ci] release v1.1.0 → v1.2.0',
        'body': '',
        'author': 'Alice Johnson',
        'author_email': 'alice.johnson@espressif.com',
    },
    {
        'rev': 'e7c1d8b6e2b549a8a5c6b3e2d9a7f5c4e2d7b6a9',
        'title': 'refactor: optimize database queries for user data retrieval',
        'body': '',
        'author': 'Charlie Green',
        'author_email': 'charlie.green@espressif.com',
    },
    {
        'rev': '05d02b594c146c89cf2c5d5c1e773da93fdcd1a3',
        'title': 'change(bump): [skip-ci] release v1.1.0 → v1.2.0.rc0',
        'body': '',
        'author': 'Jane Hunter',
        'author_email': 'jane.hunter@espressif.com',
    },
    {
        'rev': 'f8d7e1c27f0e4935bb5b5e8f5c4e3b0d4e8b6c4e',
        'title': 'docs: update API documentation for user endpoint',
        'body': '',
        'author': 'Eve Martin',
        'author_email': 'eve.martin@espressif.com',
    },
    {
        'rev': 'c3e7b3b9d7e645e9b7a4f5b7e2c8e9c4f8b5d4e9',
        'title': 'fix(frontend): correct layout issues in user profile page',
        'body': '',
        'author': 'Bob Smith',
        'author_email': 'bob.smith@espressif.com',
    },
    {
        'rev': '0b17d79a2baf456a72e04f8986469d8a69a845b1',
        'title': 'change(bump): [skip-ci] release v1.0.0 → v1.1.0',
        'body': '',
        'author': 'Ethan Mitchell',
        'author_email': 'ethan.mitchell@espressif.com',
    },
    {
        'rev': '1b7d1e7f2d8444a9bf7f5c547e8b9a3f66e4c8d1',
        'title': 'fix(api): update response codes for failed logins',
        'body': '',
        'author': 'Bob Smith',
        'author_email': 'bob.smith@espressif.com',
    },
    {
        'rev': '3d5b9c71e82b44b9b5c6a8e23f9e456fb7d5a4c1',
        'title': 'test: add integration tests for payment gateway module',
        'body': '',
        'author': 'Diana White',
        'author_email': 'diana.white@espressif.com',
    },
    {
        'rev': 'd4a8fbc34eae47c9871b5cb83e7db791f4c2c7b0',
        'title': 'revert: remove deprecated functions from auth service',
        'body': '',
        'author': 'Alice Johnson',
        'author_email': 'alice.johnson@espressif.com',
    },
    {
        'rev': '8f0b3b9f1e2a4b84a5b5c789e2c6a8d4d3b5c6f0',
        'title': 'remove: delete old caching logic from request handlers',
        'body': '',
        'author': 'Charlie Green',
        'author_email': 'charlie.green@espressif.com',
    },
    {
        'rev': 'de8dfc7d65f1e9ed8fd264dbe62380a520e9853f',
        'title': 'change(bump): [skip-ci] release v0.2.1 → v1.0.0',
        'body': '',
        'author': 'Jane Hunter',
        'author_email': 'jane.hunter@espressif.com',
    },
    {
        'rev': '7c6d91fae8bcd5239a3f8c4973e7e843f93c1be0',
        'title': 'docs(frontend): Update README for new build system integration',
        'body': '',
        'author': 'Diana White',
        'author_email': 'diana.white@espressif.com',
    },
    {
        'rev': 'c8e7a2d4b0fb55ea9b6f55b637f31af8e2f9d935',
        'title': 'ci(pipeline): add test for new database migrations',
        'body': '',
        'author': 'Charlie Green',
        'author_email': 'charlie.green@espressif.com',
    },
    {
        'rev': 'e2d5bca6e1f047a9bfcd7b72c39d3147d3b2d1ea',
        'title': 'change: refactor code to use async/await syntax',
        'body': '',
        'author': 'Eve Martin',
        'author_email': 'eve.martin@espressif.com',
    },
    {
        'rev': 'f3c34c19173b142b0fc0140a50ab5c60317e522a',
        'title': 'change(bump): [skip-ci] release v0.2.0 → v0.2.1',
        'body': '',
        'author': 'Victor Moore',
        'author_email': 'victor.moore@espressif.com',
    },
    {
        'rev': 'b2c7e8a4fc76d68baf9a5b8a7de5d3b7d4cbb745',
        'title': 'feat(api): implement new authentication mechanism with JWT tokens',
        'body': '',
        'author': 'Alice Johnson',
        'author_email': 'alice.johnson@espressif.com',
    },
    {
        'rev': '4b1d62bfc7a942e8b123b17f8cba07d5ec4de1e6',
        'title': 'fix: resolve null pointer exception in user session management',
        'body': '',
        'author': 'Bob Smith',
        'author_email': 'bob.smith@espressif.com',
    },
    {
        'rev': '18e5faebc94d1aecc3fd7c8cfb63d5197800041f',
        'title': 'change(bump): [skip-ci] release v0.1.0 → v0.2.0',
        'body': '',
        'author': 'Nina Shaw',
        'author_email': 'nina.shaw@espressif.com',
    },
    {
        'rev': 'b2c7e8a4fc76d68baf9a5b8a7de5d3b7d4cbb745',
        'title': 'feat(api): implement new authentication mechanism with JWT tokens',
        'body': '',
        'author': 'Alice Johnson',
        'author_email': 'alice.johnson@espressif.com',
    },
    {
        'rev': '4b1d62bfc7a942e8b123b17f8cba07d5ec4de1e6',
        'title': 'fix: resolve null pointer exception in user session management',
        'body': '',
        'author': 'Bob Smith',
        'author_email': 'bob.smith@espressif.com',
    },
    {
        'rev': '7d1f8c5bd1b56a65e30e6bb7f5dd1c2c1b0e5d4c',
        'title': 'ci(init): initialize project with empty commit, initial tag',
        'body': '',
        'author': 'Tomas Sebestik',
        'author_email': 'tomas.sebestik@espressif.com',
    },
]


TAGS = [
    ('v1.3.0', '22c4820bd927ad017649bcf6e8d03e30ddc946e9', '2024-08-30'),
    ('v1.2.0', 'd25d90e96d5f6bdeeca1f340cce9f7b87f7c8c0e', '2024-07-15'),
    ('v1.2.0.rc0', '05d02b594c146c89cf2c5d5c1e773da93fdcd1a3', '2024-06-10'),
    ('v1.1.0', '0b17d79a2baf456a72e04f8986469d8a69a845b1', '2024-05-23'),
    ('v1.0.0', 'de8dfc7d65f1e9ed8fd264dbe62380a520e9853f', '2024-04-12'),
    ('v0.2.1', 'f3c34c19173b142b0fc0140a50ab5c60317e522a', '2024-03-29'),
    ('v0.2.0', '18e5faebc94d1aecc3fd7c8cfb63d5197800041f', '2024-03-02'),
    ('v0.1.0', '7d1f8c5bd1b56a65e30e6bb7f5dd1c2c1b0e5d4c', '2024-02-15'),
]


@pytest.fixture
def gitcommits() -> list[git.GitCommit]:
    return [git.GitCommit(**commit) for commit in COMMITS_DATA]


@pytest.fixture
def tags() -> list[git.GitTag]:
    tags = [git.GitTag(*tag) for tag in TAGS]
    return tags


@pytest.fixture
def render_changelog(config, gitcommits, tags, capsys, mocker: MockerFixture):
    """
    Generate a changelog using the same flow as the cz changelog command.
    """

    def fixture(unreleased: bool = True, **kwargs) -> str:
        incremental = kwargs.get('incremental', config.settings.get('incremental', False))

        # Mock Git commits based on whether it's incremental or full
        mocker.patch('commitizen.git.get_commits', return_value=gitcommits[:4] if incremental else gitcommits)
        mocker.patch('commitizen.git.get_tags', return_value=tags)

        kwargs['dry_run'] = True
        kwargs['incremental'] = incremental
        kwargs['unreleased_version'] = unreleased

        cmd = Changelog(config, kwargs)
        mocker.patch.object(cmd.changelog_format, 'get_metadata').return_value = Metadata(latest_version='1.3.0')

        capsys.readouterr()

        try:
            cmd()
        except DryRunExit:
            pass

        return capsys.readouterr().out

    return fixture


### Czespressif plugin
### -------------------------------------------------


def test_changelog_czespressif_full(render_changelog, snapshot):
    """
    DEFAULT SETTINGS - Full changelog
    Emulates command:   'cz changelog' ('cz ch')
    With pyproject.toml:
                        [tool.commitizen]
                            name                       = "czespressif"
                            changelog_merge_prerelease = true
                            tag_format                 = "v$version"
    """
    assert render_changelog() == snapshot


@pytest.mark.settings(incremental=True)
def test_changelog_czespressif_incremental(render_changelog, snapshot):
    """
    DEFAULT SETTINGS - Incremental changelog
    Emulates command:   'cz changelog v1.3.0' ('cz ch v1.3.0')
                        'cz changelog v1.2.0..v1.3.0' ('cz ch v1.2.0..1.3.0')
                        'cz bump'
    With pyproject.toml:
                        [tool.commitizen]
                            name                       = "czespressif"
                            changelog_merge_prerelease = true
                            tag_format                 = "v$version"
    """
    assert render_changelog() == snapshot


@pytest.mark.settings(use_emoji=False)
def test_changelog_czespressif_full_no_emoji(render_changelog, snapshot):
    """
    WITHOUT EMOJI - Full changelog
    Emulates command:   'cz changelog' ('cz ch')
    With pyproject.toml:
                        [tool.commitizen]
                            name                       = "czespressif"
                            changelog_merge_prerelease = true
                            tag_format                 = "v$version"
                            use_emoji                  = false
    """
    assert render_changelog() == snapshot


@pytest.mark.settings(use_emoji=False)
@pytest.mark.settings(incremental=True)
def test_changelog_czespressif_incremental_no_emoji(render_changelog, snapshot):
    """
    WITHOUT EMOJI - Incremental changelog
    Emulates command:   'cz changelog v1.3.0' ('cz ch v1.3.0')
                        'cz changelog v1.2.0..v1.3.0' ('cz ch v1.2.0..1.3.0')
                        'cz bump'
    With pyproject.toml:
                        [tool.commitizen]
                            name                       = "czespressif"
                            changelog_merge_prerelease = true
                            tag_format                 = "v$version"
                            use_emoji                  = false
    """
    assert render_changelog() == snapshot


### WITHOUT 'czespressif' plugin
### -------------------------------------------------


@pytest.mark.settings(name='cz_conventional_commits')  # This is the default value for Commitizen
def test_changelog_cz_default_full(render_changelog, snapshot):
    """
    DEFAULT SETTINGS COMMITIZEN WITHOUT czespressif PLUGIN - Full changelog
    Emulates command:   'cz changelog' ('cz ch')
    With pyproject.toml:
                        [tool.commitizen]
                            changelog_merge_prerelease = true
                            tag_format                 = "v$version"
    """
    assert render_changelog() == snapshot


@pytest.mark.settings(name='cz_conventional_commits')  # This is the default value for Commitizen
def test_changelog_cz_default_incremental(render_changelog, snapshot):
    """
    DEFAULT SETTINGS COMMITIZEN WITHOUT czespressif PLUGIN - Incremental changelog
    Emulates command:   'cz changelog v1.3.0' ('cz ch v1.3.0')
                        'cz changelog v1.2.0..v1.3.0' ('cz ch v1.2.0..1.3.0')
                        'cz bump'
    With pyproject.toml:
                        [tool.commitizen]
                            changelog_merge_prerelease = true
                            tag_format                 = "v$version"
    """
    assert render_changelog(incremental=True) == snapshot
