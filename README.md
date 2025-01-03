<a href="https://www.espressif.com">
    <img src="https://www.espressif.com/sites/all/themes/espressif/logo-black.svg" alt="Espressif logo" title="Espressif" align="right" height="20" />
</a>

# Commitizen Plugin `czEspressif`

This is a plugin for Commitizen that makes it easy to create and maintain a well-organized and good-looking `CHANGELOG.md`. It also takes care of version bumping and helps you write commit messages that follow Espressif standards.

All of this with minimal config and setup, so your `pyproject.toml` file stays clean and simple.

<!-- GitHub Badges -->

<div align="center">
  <p>
    <hr>
    <a href="https://github.com/espressif/cz-plugin-espressif/releases">
      <img alt="GitHub Release"  src="https://img.shields.io/github/v/release/espressif/cz-plugin-espressif? display_name=release&logo=github&logoColor=white&label=Release">
    </a>
    <a href="https://pypi.org/project/czespressif/">
      <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/czespressif?logo=pypi&logoColor=white&label=Pythons&link=https%3A%2F%2Fpypi.org%2Fproject%2Fczespressif%2F">
    </a>
    <img alt="Static Badge" src="https://img.shields.io/badge/pip%20install-czespressif-black?logo=python&logoColor=white">
    <a href="/LICENSE">
      <img alt="Project License" src="https://img.shields.io/pypi/l/czespressif"/>
    </a>
    <br>
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/espressif/cz-plugin-espressif?logo=github&label=Contributors&color=purple">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/espressif/cz-plugin-espressif?logo=git&logoColor=white&label=Commits&color=purple">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/espressif/cz-plugin-espressif?logo=git&logoColor=white&label=Last%20commit">
    <a href="https://pypi.org/project/czespressif/">
      <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/czespressif?logo=pypi&logoColor=white&label=PyPI%20downloads&color=blue&cacheSeconds=3600&link=https%3A%2F%2Fpypi.org%2Fproject%2Fczespressif%2F">
    </a>
    <br>
    <a href="https://github.com/espressif/cz-plugin-espressif/actions/workflows/plugin-tests.yml">
      <img alt="GitHub workflow Tests Pytest" src="https://img.shields.io/github/actions/workflow/status/espressif/cz-plugin-espressif/.github%2Fworkflows%2Fplugin-tests.yml?branch=master&logo=pytest&logoColor=white&label=Tests&link=https%3A%2F%2Fgithub.com%2Fespressif%2Fcz-plugin-espressif%2Factions%2Fworkflows%2Fplugin-tests.yml">
    </a>
    <a href="https://github.com/espressif/cz-plugin-espressif/actions/workflows/sync-jira.yml">
      <img alt="GitHub workflow SyncJira" src="https://img.shields.io/github/actions/workflow/status/espressif/cz-plugin-espressif/.github%2Fworkflows%2Fsync-jira.yml?branch=master&logo=jirasoftware&label=Sync with Jira&link=https%3A%2F%2Fgithub.com%2Fespressif%2Fcz-plugin-espressif%2Factions%2Fworkflows%2Fsync-jira.yml">
    </a>
    <a href="https://github.com/espressif/cz-plugin-espressif/actions/workflows/code-ql.yml">
      <img alt="GitHub workflow CodeQL" src="https://img.shields.io/github/actions/workflow/status/espressif/cz-plugin-espressif/.github%2Fworkflows%2Fcode-ql.yml?branch=master&label=CodeQL">
    </a>
  </p>
  <small>
    <b>
      <a href="https://github.com/espressif/cz-plugin-espressif/issues/new?assignees=&labels=Type%3A+Bug&projects=&template=01-BUG-REPORT.yml">Report bug</a>
      ·
      <a href="https://github.com/espressif/cz-plugin-espressif/issues/new?assignees=&labels=Type%3A+Feature\+Request&projects=&template=02-FEATURE-REQUEST.yml">Request Feature</a>
    </b>
  </small>
  <hr>
</div>

- [Commitizen plugin czEspressif](#commitizen-plugin-czespressif)
  - [Features](#features)
  - [Compatibility](#compatibility)
  - [Install](#install)
  - [Usage](#usage)
    - [Create Changelog file](#create-changelog-file)
    - [Bump Release version](#bump-release-version)
    - [GitHub Action for Automated Release Creation](#github-action-for-automated-release-creation)
    - [Create commit messages](#create-commit-messages)
    - [Examples of good commit messages](#examples-of-good-commit-messages)
  - [Configuration](#configuration)
    - [Minimal setup](#minimal-setup)
    - [Optimal setup](#optimal-setup)
    - [Additional configurable parameters](#additional-configurable-parameters)
  - [Solving Troubles](#solving-troubles)
  - [Pre-commit hook (beta)](#pre-commit-hook-beta)
  - [Contributing](#contributing)
  - [License](#license)
  - [Credits](#credits)

---

## Features

- Can be almost zero-config but offers many customization options if your project needs it.
- Predefined **CHANGELOG template** with default categories _Breaking Changes / New Features / Bug Fixes / Documentation / Code Refactoring / Removals_.
- The CHANGELOG automatically displays commits and the authors of those commits.
- The default order in the changelog categories lists commits with a scope first, followed by the rest, both groups sorted alphabetically.
- Predefined **Release Notes template** that can be used in an automated release workflow.
- `cz commit` command with default Espressif commit types, aligned with the Espressif pre-commit linter.
- You can use pre-commit hook that triggers a local changelog update (Unreleased section) when version files change.

---

## Compatibility

[This plugin](https://pypi.org/project/czespressif/) requires Python 3.9 or higher. It should run on pretty much any anything (Linux, Mac, Windows, amd64, aarch64).

If you encounter issues with a specific architecture or OS, please [report it here](https://github.com/espressif/cz-plugin-espressif/issues/new?assignees=&labels=Type%3A+Bug&projects=&template=01-BUG-REPORT.yml), and we will try to address it as soon as possible.

---

## Install

Install with `pip` or your favorite package manager:

```sh
pip install czespressif
```

Then add this snippet to \`pyproject.toml:

```ini
[tool.commitizen]
   name            = "czespressif"
   bump_message    = 'change(bump): release $current_version → $new_version [skip-ci]'
```

And verify that installation and setup was successful by showing the example.

```sh
cz example
```

> \[!TIP\]
> You can also add it to your project `dev` dependencies (suggested) and run the sync command (`pipenv sync`, `pip-sync`, `poetry install`, ...).
>
> commitizen itself is in the plugin's dependencies, so pip will take care of everything.

> \[!WARNING\]
> Don't try to install it system-wide with `pipx`; it likely won't work as expected.
> (This option will be explored in the future, and once a solution is found, we will update this recommendation.)

---

## Usage

> \[!TIP\]
> You can check the implementation of this command in the GitHub workflow [.github/workflows/create-release.yml](.github/workflows/create-release.yml) if you're interested.
> In this project's [tests/**snapshots**/test_changelog/](tests/__snapshots__/test_changelog/) directory, we store snapshots used for automated testing. These snapshots **also serve as examples of the plugin's output**.
> You can explore them and compare the plugin output (`test_changelog_czespressif_*.md`) with the default Commitizen output (`test_changelog_cz_default_*.md`), which is generated when our plugin is not used.

### Create Changelog File

If a changelog already exists in your project, make sure you have staged or committed its latest version.

This command turns your old changelog into a nicely organized template based on the [Keep a Changelog standard](https://keepachangelog.com/en/1.1.0/).

```sh
cz changelog
```

### Bump Release Version

Is better to first run:

```sh
cz bump --dry-run
```

This only shows the future version and the part of the changelog that will be updated. When all ok, do the same without `--dry-run` flag.

### GitHub Action for Automated Release Creation

In automated scenarios, such as GitHub Actions workflows, you may want to create project releases automatically. This can be easily achieved by parsing the changelog to extract the "Release notes" relevant to the current release.

In this repository, there is a GitHub workflow (`.github/workflows/create-release.yml`) that follows this strategy. To trigger a release, the repository admin simply needs to push a release tag to the origin (GitHub).
This triggers the workflow, which builds all Python binaries for all combinations of Python versions, operating systems, and architectures. It then parses the changelog to extract the release notes (only the section related to the current release, without any headers, footers, etc.), creates a GitHub release, and uploads the binaries both to the GitHub release and the PyPI registry.

The following command generates the changelog for the release version v4.8.0, using the internal template for release notes and writing the partial changelog to a file:

```sh
cz changelog v4.8.0 --template="RELEASE_NOTES.md.j2" --file-name="Release_notes.md"

```

**Release notes custom footer**: You can append a custom footer to the end of the release notes snippet. For example, if you want to include a link to something important for your project, or maybe some GitHub badges, and so on, you can do that.

You can check [example without a footer (default)](docs/Release_notes_example.md) and [example with a custom footer](docs/Release_notes_example_with_footer.md).

> \[!IMPORTANT\]
> Note that the custom template for release notes is part of the czespressif plugin, not the target (your project) repository.
> Any custom settings you define for the changelog locally in the project configuration will also apply to the release notes. For example, if you change the order of sections in the changelog, the release notes will reflect that change as well.
>
> This approach ensures consistent visual styling and allows repository admins to configure everything in one place.

> \[!TIP\]
> You can check the implementation of this command in the GitHub workflow [.github/workflows/create-release.yml](.github/workflows/create-release.yml) if you're interested.

### Create Commit Messages

In case anyone actually prefers this way of creating commit messages, the command in this plugin is aligned with the Espressif commit linter and DangerJS linters.:

```sh
cz commit
```

```txt
? Select the type of change you are committing (Use arrow keys)
 » feat                     ✨ A new feature
   fix                      🐛 A bug fix
   change                   🏗️ A change made to the codebase.
   docs                     📖 Documentation only change
   test                     🚦  Adding missing or correcting existing tests
   ci                       ⚙️ Changes to CI configuration files and scripts
   refactor                 🔧 A changeset neither fixing a bug nor adding a feature
   revert                   🔙 Revert one or more commits
   remove                   🗑️ Removing code or files
```

### Examples of Good Commit Messages

If you are unsure about the commit message standard, run:

```sh
cz example
```

This will bring up a complete example of good commit messages and commit schema in the terminal.

---

## Configuration

Config is accepted in `pyproject.toml` (priority, following example), `.cz.toml`, `.cz.json`, `cz.json`, `.cz.yaml`, `cz.yaml`, and `cz.toml`.

### Minimal Setup

> \[!TIP\]
> Try to be minimalistic with custom configs. The best approach is to keep the defaults, so all Espressif projects maintain the same look and feel.
> Also, you will save yourself troubles with non-standard setups.

```ini
[tool.commitizen]
   name                      = "czespressif"
   bump_message              = 'change(bump): release $current_version → $new_version [skip-ci]'
```

### Optimal Setup

```ini
[tool.commitizen]
  name                       = "czespressif"
  bump_message               = 'change(bump): release $current_version → $new_version [skip-ci]'

  # see commitizen docs, following are standard configs
  annotated_tag              = true
  changelog_merge_prerelease = true
  tag_format                 = "v$version"
  update_changelog_on_bump   = true
  version                    = "1.2.3"
  version_files              = ["<src>/__init__.py:__version__"]
  version_provider           = "commitizen"

```

### Additional Configurable Parameters

```ini
[tool.commitizen]
    ...

    # - Section emojis in the changelog, emojis in CLI command `cz commit` -
    # Default: true; false = do not display emojis
    # Note: Emojis are never added in the commit messages.
    use_emoji = false

    # - Custom text of changelog title -
    # Note: "" (empty string) disables title
    changelog_title = "Our changelog"

    # - Custom text of changelog header -
    # Note: "" (empty string) disables header
    changelog_header = "This is our changelog.\nAll cool things we do are here.\n\nPlease read it."

    # - Custom text of changelog footer -
    # Note: "" (empty string) disables footer
    changelog_footer = "This is the end of our changelog.\n\nMore cool things are coming."

    # - Horizontal lines between release sections in the changelog -
    # Default: true; false = removes lines
    changelog_section_line = false  # default (true); false = removes horizontal lines between releases

    # - Section "Unreleased" in the changelog -
    # Default: true; false = removes section Unreleased, keeps only releases
    changelog_unreleased = false

    # - Authors of the changes (commits) in the changelog -
    # Default: true; false = do not display authors
    changelog_show_authors = false

    # - Commit numbers (short SHA) in the changelog -
    # Default: true; false = do not display commit numbers
    changelog_show_commits = false

    # - Change orders in which sections displays in the changelog -
    # Default: this example is default
    change_type_order = [ # with enabled emojis
        '🚨 Breaking Changes',
        '✨ New Features',
        '🐛 Bug Fixes',
        '📖 Documentation',
        '🔧 Code Refactoring',
        '🗑️ Removals',
        '🏗️ Changes',  # in default not in the changelog
        '⚙️ CI and Project Settings',    # in default not in the changelog
        '🚦 Testing',  # in default not in the changelog
        '🔙 Reverted',  # in default not in the changelog
    ]

    change_type_order = [  # same thing, with disabled emojis
        'Breaking Changes',
        'New Features',
        'Bug Fixes',
        'Documentation',
        'Code Refactoring',
        'Removals',
        'Changes',  # in default not in the changelog
        'CI and Project Settings',  # in default not in the changelog
        'Testing',  # in default not in the changelog
        'Reverted',  # in default not in the changelog
    ]

    # - Redefine which types are shown in the changelog -
    # Note: You need to list here ALL types that you want to have in the changelog - included default ones
    # Note: The order in this list doesn't matter — if you want to change the sections' order too, use with "change_type_order."
    types_in_changelog = ["feat", "fix", "refactor", "style", "ci"]


    # - Custom text that you can append to release notes output -
    # Default: Null (in default there is no custom footer )
    release_notes_footer = """Thanks to <FILL OUT CONTRIBUTORS>, and others for contributing to this release!"""

    # - Add extra commit types for 'cz commit' and to the changelog (sections) -
    # Note: If you are working with custom commit types, ensure your commit linter and PR/MR linter is set same way
    [[tool.commitizen.extra_types]]
        type        = "style"
        heading     = "Code Style"
        emoji       = "🎨"
        description = "Changes that do not affect the meaning of the code (white-space, formatting, etc.)"
        bump        = "PATCH"
        changelog   = true
```

---

## Solving Troubles

The plugin `czespressif` has `commitizen` as its dependency, so users only need to install `czespressif`, and that will automatically install the proper version of `commitizen`. This plugin requires at least version 3.29 of `commitizen` to work properly. Older versions either cause errors like this:

```log
The committer has not been found in the system.

Try running 'pip install czespressif'
```

... or `czespressif` plugin partially works but behaves in weird and unexpected ways.

If you encounter this error, it probably means that you have a conflicting version of commitizen installed on your system, and this old version is prioritized in your system path.

You can copy and paste this snippet into your terminal to check if this is the case:

```sh
clear;if command -v cz &> /dev/null; then
    cz_version=$(cz version | awk '{print $NF}')
    if [ "$(printf '%s\n' "3.29" "$cz_version" | sort -V | head -n1)" = "3.29" ]; then
        echo "Commitizen version $cz_version is OK."
    else
        echo "Commitizen version $cz_version is too old. Found at $(which cz)."
        echo "Please uninstall it with 'pip uninstall commitizen' or 'pipx uninstall commitizen'."
    fi
else
    echo "No Commitizen found, but you are not in a virtual environment."
    echo "Consider creating/activating a virtual environment first and installing by 'pip install czespressif'."
fi
```

> \[!TIP\]
> For each Python project, use a virtual environment. If you install everything with pip to the system Python, you risk running into unsolvable dependency issues and possibly breaking some system tools.
>
> If your project isn’t a Python project and you don’t care about python virtual envs, at least ensure you don’t have multiple outdated versions of some Python packages, such as commitizen in this case.

---

## Pre-Commit Hook (Beta)

To automatically keep your changelog's "Unreleased" section up to date, add the following to your `.pre-commit-config.yaml` file:

```yaml
- repo: https://github.com/espressif/cz-plugin-espressif
  rev: ''
  hooks:
    - id: update-changelog
```

Next, run the following command to fetch the latest version (`rev:`):

```sh
pre-commit autoupdate --repo https://github.com/espressif/cz-plugin-espressif
```

If you have already set `default_install_hook_types`, then include `pre-push` in the list. Otherwise, add the following to your `.pre-commit-config.yaml` file:

```yaml
default_install_hook_types: [pre-commit, pre-push]
```

After installing the hook, it runs automatically before you pushing commits to the repository. It updates the changelog with the latest commits. If the push failed because of the hook, don't forget to add the updated changelog to the commit and push again.

---

## Contributing

We welcome contributions from the community! Please read the [Contributing Guide](CONTRIBUTING.md) to learn how to get involved.

---

## License

This PROJECT is licensed under the [Apache 2.0 License](LICENSE).

---

## Credits

This was inspired by the project [Emotional](https://github.com/noirbizarre/emotional), created by [Axel H. / @noirbizarre](https://github.com/noirbizarre).

- If you are looking for **similar and customizable plugin for projects outside Espressif** organization, you should definitely try [Emotional](https://github.com/noirbizarre/emotional).

- If you are learning Python and want to write clean and well-organized, pro-level code, you should definitely check out [Emotional](https://github.com/noirbizarre/emotional).

---
