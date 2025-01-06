<a href="https://www.espressif.com">
    <img src="https://www.espressif.com/sites/all/themes/espressif/logo-black.svg" align="right" height="20" />
</a>

# CHANGELOG

> All notable changes to this project are documented in this file.
> This list is not exhaustive - only important changes, fixes, and new features in the code are reflected here.

<div align="center">
    <a href="https://keepachangelog.com/en/1.1.0/">
        <img alt="Static Badge" src="https://img.shields.io/badge/Keep%20a%20Changelog-v1.1.0-salmon?logo=keepachangelog&logoColor=black&labelColor=white&link=https%3A%2F%2Fkeepachangelog.com%2Fen%2F1.1.0%2F">
    </a>
    <a href="https://www.conventionalcommits.org/en/v1.0.0/">
        <img alt="Static Badge" src="https://img.shields.io/badge/Conventional%20Commits-v1.0.0-pink?logo=conventionalcommits&logoColor=black&labelColor=white&link=https%3A%2F%2Fwww.conventionalcommits.org%2Fen%2Fv1.0.0%2F">
    </a>
    <a href="https://semver.org/spec/v2.0.0.html">
        <img alt="Static Badge" src="https://img.shields.io/badge/Semantic%20Versioning-v2.0.0-grey?logo=semanticrelease&logoColor=black&labelColor=white&link=https%3A%2F%2Fsemver.org%2Fspec%2Fv2.0.0.html">
    </a>
</div>
<hr>

## v1.3.0 (2024-10-07)

### ✨ New Features

- **pre-commit**: run in pre-push stage *(Fu Hanxi - 11c2d0a)*

### 🐛 Bug Fixes

- pre-commit entry to support custom args *(Fu Hanxi - 36c6c4a)*

---

## v1.2.0 (2024-10-02)

### ✨ New Features

- **test-suite**: add tests changelog/plugin, compare with snapshots (syrupy module) *(Tomas Sebestik - c4d78e3)*

### 🐛 Bug Fixes

- **changelog**: fix double title, header and footer on 'cz bump' *(Tomas Sebestik - b5a1227)*

### 📖 Documentation

- **contributing**: update docs for setup dev environment and testing *(Tomas Sebestik - dfca4d6)*

### 🔧 Code Refactoring

- **python-3.9**: refactor syntax and typing for python 3.9 *(Tomas Sebestik - e5a83c6)*

---

## v1.1.0 (2024-09-24)

### ✨ New Features

- **changelog**: custom template for release notes (GH action) *(Tomas Sebestik - 19e8cec)*

### 🐛 Bug Fixes

- **github-actions**: update create-release.yml, missing "v" in version
- (dependabot): update dependabot config file, team reviewers
- (justfile): add recipe for local cleanup temp, manual tests *(Tomas Sebestik - f601dbf)*

### 📖 Documentation

- **readme**: docs to automatic process of "Release notes" *(Tomas Sebestik - 6a18980)*

---

## v1.0.1 (2024-09-10)

### 🐛 Bug Fixes

- **pre-commit**: change lang from system to python to be able install deps *(Tomas Sebestik - 7443af0)*

---

## v1.0.0 (2024-09-10)

### ✨ New Features

- **plugin**: add plugin, commit message questions, changelog template (#1) *(Tomas Sebestik - f2fa815)*

---

<div align="center">
    <small>
        <b>
            <a href="https://www.github.com/espressif/cz-plugin-espressif">Commitizen Espressif plugin</a>
        </b>
    <br>
        <sup><a href="https://www.espressif.com">Espressif Systems CO LTD. (2025)</a><sup>
    </small>
</div>
