set quiet := true
set shell := ["bash", "-c"]
set positional-arguments := true

# Private default task
[private]
default:
    just --choose --unsorted

# Gracefully exit just chooser
exit:
    exit 0

build-install:
    pip uninstall -y czespressif
    python -m build
    pip install .
    cz example
    pip list | grep czespressif

install:
    pip uninstall -y czespressif
    pip install -e .
    cz example
    pip list | grep czespressif

# Remove virtual environment
remove-venv:
    rm -rf venv
    rm -rf .venv

# Reinstall development dependencies in virtual environment
reinstall-venv:
    just activate-venv && pip install -e '.[dev]'

# Clean temporary and cache files
clean-temps:
    find . -type d \( -name '.mypy_cache' -o -name '.ruff_cache' -o -name 'build' -o -name 'dist' \) -exec rm -rf {} +

# Set up the environment: activate and reinstall
setup-env:
    just activate-venv && just reinstall-venv

# List outdated Python packages
pip-list-outdated:
    just activate-venv && pip list --outdated

# List Python packages excluding editable
pip-list-exlude-editable:
    just activate-venv && pip list --exclude-editable

pip-list-search-installed PACKAGE:
    just activate-venv && pip list --format=columns | grep '{{PACKAGE}}'

# Run pre-commit checks
pre-commit-all-files:
    just activate-venv && pre-commit run --all-files

# Run pre-commit checks on staged files
pre-commit-staged:
    just activate-venv && pre-commit run

# Run pre-commit checks and specify files
pre-commit-files FILES:
    just activate-venv && pre-commit run --files {{FILES}}

# Autoupdate pre-commit hooks
pre-commit-autoupdate:
    just activate-venv && pre-commit autoupdate

# Reuse the last commit message, opening it in the editor for modification
git-fix-message:
    git commit --edit --file=$(git rev-parse --git-dir)/COMMIT_EDITMSG
