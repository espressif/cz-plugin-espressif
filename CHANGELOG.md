# CHANGELOG

> All notable changes to this project are documented in this file.
> This list is not exhaustive - only important changes, fixes, and new features in the code are reflected here.

<sub>The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),     [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and     [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
</sub>

---

## Unreleased

### ✨ New features

- **changelog**: custom template for release notes (GH action) *(Tomas Sebestik - 19e8cec)*

### 🐛 Bug fixes

- **github-actions**: update create-release.yml, missing "v" in version
- (dependabot): update dependabot config file, team reviewers
- (justfile): add recipe for local cleanup temp, manual tests *(Tomas Sebestik - f601dbf)*

### 📖 Documentation

- **readme**: docs to automatic process of "Release notes" *(Tomas Sebestik - 6a18980)*

---

## v1.0.1 (2024-09-10)

### 🐛 Bug fixes

- **pre-commit**: change lang from system to python to be able install deps *(Tomas Sebestik - 7443af0)*

---

## v1.0.0 (2024-09-10)

### ✨ New features

- **plugin**: add plugin, commit message questions, changelog template (#1) *(Tomas Sebestik - f2fa815)*

---

**[Espressif Systems CO LTD. (2024)](https://www.espressif.com/)**

- [Commitizen tools plugin with Espressif code style](https://www.github.com/espressif/cz-plugin-espressif)
- [Espressif Coding Standards and Best Practices](https://www.github.com/espressif/standards)
