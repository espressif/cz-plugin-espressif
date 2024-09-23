set quiet := true
set positional-arguments := true

[private]
default:
    just --choose --unsorted

exit:
    exit 0

get-versions:
    pip list | grep -E 'cz|commitizen'

build-install:
    pip uninstall -y czespressif
    python -m build
    pip install .
    cz example
    just get-versions

dry-bump:
    cz bump --dry-run

example:
    cz example

info:
    cz info

schema:
    cz schema

changelog-show:
    cz changelog --dry-run

release-notes-show:
    cz changelog v1.0.0 --template="RELEASE_NOTES.md.j2" --dry-run

changelog-file:
    cz changelog --file-name="CHANGELOG-output.md"

release-notes-file:
    cz changelog v1.0.0 --template="RELEASE_NOTES.md.j2" --file-name="Release_notes.md"

tests:
    echo "Maximize terminal ...." && just get-versions && sleep 2 && clear
    just dry-bump && sleep 3 && clear
    just info && sleep 2 && clear
    just example && sleep 2 && clear
    just schema && sleep 2 && clear
    just changelog-show && sleep 5 && clear
    just release-notes-show && sleep 5 && clear
    echo "Resize terminal, tests ends ...." && just get-versions && sleep 2 && clear

live-install:
    pip uninstall -y czespressif
    pip install -e '.[dev]'
    pip install --upgrade pip
    cz example
    just get-versions

clean-temps:
    rm -rf \
        dist \
        .pytest_cache \
        .mypy_cache \
        .coverage \
        .coverage.* \
        .ruff_cache \
        *.egg-info \
        CHANGELOG-output.md \
        Release_notes.md \
        build \
        **/__pycache__/ \
        :
