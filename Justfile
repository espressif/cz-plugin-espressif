set quiet := true
set positional-arguments := true

[private]
default:
    just --choose --unsorted

exit:
    exit 0

build-install:
    pip uninstall -y czespressif
    python -m build
    pip install .
    cz example
    pip list | grep -E 'cz|commitizen'

dry-bump:
    clear
    cz bump --dry-run

example:
    clear
    cz example

changelog:
    clear
    cz changelog --file-name="CHANGELOG-output.md"

release-notes:
    clear
    cz changelog v1.0.0 --template="RELEASE_NOTES.md.j2" --file-name="Release_notes.md"

live-install:
    pip uninstall -y czespressif
    pip install -e . '[.dev]'
    cz example
    pip list | grep -E 'cz|commitizen'

clean-temps:
    rm -rf .pytest_cache .mypy_cache .nox .ruff_cache .tox build dist
