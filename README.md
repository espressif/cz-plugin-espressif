<div align="center">
  <h1>Commitizen Espressif style plugin </h1>
    Commitizen tools plugin with Espressif code style
  <br>
  <br>

[![Release][release-badge]][release-url] [![Pre-commit][pre-commit-badge]][pre-commit-url] [![Conventional Commits][conventional-badge]][conventional-url]

</div>
<hr>

- [Introduction](#introduction)
- [Install](#install)
  - [Build Changelog](#build-changelog)
  - [Bump Release version](#bump-release-version)
  - [Write commit message](#write-commit-message)
  - [Example](#example)
- [Configuration](#configuration)
  - [Minimal setup](#minimal-setup)
  - [Optimal setup](#optimal-setup)
  - [Additional configurable parameters](#additional-configurable-parameters)
- [Pre-commit hook](#pre-commit-hook)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

This is a plugin for Commitizen that makes it easy to create and maintain a well-organized and good-looking `CHANGELOG.md`.

It also takes care of version bumping and helps you write commit messages that follow Espressif standards.

All of this with minimal config and setup, so your `pyproject.toml` file stays clean and simple.

---

## Install

Of course, you have already created and activated a Python virtual environment... then:

```sh
pip install czespressif
```

.... and add snippet from [Minimal setup](#minimal-setup) - that's it 🤝.

You can also add it to your project `dev` dependencies (suggested) and run the sync command (`pipenv sync`, `pip-sync`, `poetry install`, ...).

Commitizen itself is in the plugin's dependencies, so pip will take care of everything.

> \[!WARNING\]
> Don't try to install it system-wide with `pipx`.
>
> This is a plugin, and that's probably not going to work as you expect.

### Build Changelog

If a changelog already exists in your project, make sure you have staged or committed its latest version.

This command turns your old changelog into a nicely organized template based on the Keep Changelog standard.

```sh
cz changelog
```

### Bump Release version

Is better to first run:

```sh
cz bump --dry-run
```

This only shows the future version and the part of the changelog that will be updated. When all ok, do the same without `--dry-run` flag.

### Write commit message

In case anyone actually prefers this way of creating commit messages, the command:

```sh
cz commit
```

in this plugin is aligned with the Espressif commit linter and DangerJS linters. You can give it a try...

```
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

### Example

If you are unsure about the commit message standard, hit:

```sh
cz example

```

This will bring up a complete example of good commit messages and commit schema in the terminal.

---

## Configuration

Config is accepted in `pyproject.toml` (priority, following example), `.cz.toml`, `.cz.json`, `cz.json`, `.cz.yaml`, `cz.yaml`, and `cz.toml`.

### Minimal setup

> \[!TIP\]
> Try to be minimalistic with custom configs. The best approach is to keep the defaults, so all Espressif projects maintain the same look and feel.
> Also, you will save yourself troubles with non-standard setups.

```ini
[tool.commitizen]
   name            = "czespressif"
   bump_message    = 'change(bump): release $current_version → $new_version [skip-ci]'
```

### Optimal setup

```ini
[tool.commitizen]
  name            = "czespressif"
  bump_message    = 'change(bump): release $current_version → $new_version [skip-ci]'

  # see commitizen docs, following are standard configs
  annotated_tag = true
  changelog_merge_prerelease = true
  tag_format = "v$version"
  update_changelog_on_bump = true

```

### Additional configurable parameters

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
        '🚨 Breaking changes',
        '✨ New features',
        '🐛 Bug fixes',
        '📖 Documentation',
        '🔧 Code refactoring',
        '🗑️ Removals',
        '🏗️ Changes',  # in default not in the changelog
        '⚙️ CI and project settings',    # in default not in the changelog
        '🚦 Testing',  # in default not in the changelog
        '🔙 Reverted',  # in default not in the changelog
    ]

    change_type_order = [  # same thing, with disabled emojis
        'Breaking changes',
        'New features',
        'Bug fixes',
        'Documentation',
        'Code refactoring',
        'Removals',
        'Changes',  # in default not in the changelog
        'CI and project settings',  # in default not in the changelog
        'Testing',  # in default not in the changelog
        'Reverted',  # in default not in the changelog
    ]

    # - Redefine which types are shown in the changelog -
    # Note: You need to list here ALL types that you want to have in the changelog - included default ones
    # Note: The order in this list doesn't matter — if you want to change the sections' order too, use with "change_type_order."
    types_in_changelog = ["feat", "fix", "refactor", "style", "ci"]

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

## Pre-commit hook

To automatically keep your changelog's "Unreleased" section up to date, add the following to your `.pre-commit-config.yaml` file:

```yaml
- repo: https://github.com/espressif/cz-plugin-espressif
  rev: ""
  hooks:
    - id: update-changelog
```

Next, run the following command to fetch the latest version (`rev:`):

```sh
pre-commit autoupdate --repo https://github.com/espressif/cz-plugin-espressif
```

## Contributing

We welcome contributions from the community! Please read the [Contributing Guide](CONTRIBUTING.md) to learn how to get involved.

## License

This repository is licensed under the [Apache 2.0 License](LICENSE).

---

<!-- GitHub Badges -->

[conventional-badge]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square
[conventional-url]: https://conventionalcommits.org
[pre-commit-badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit&logoColor=white
[pre-commit-url]: https://github.com/pre-commit/pre-commit
[release-badge]: https://img.shields.io/github/v/release/espressif/cz-plugin-espressif
[release-url]: https://github.com/espressif/cz-plugin-espressif/releases
