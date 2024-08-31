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

# Activate virtual environment
activate-venv:
    if [ -d "venv" ]; then source venv/bin/activate; else echo "Virtual environment not found. Please create it first."; fi

# Reinstall development dependencies in virtual environment
reinstall-venv:
    just activate-venv && pip install -e '.[dev]'

# Clean temporary and cache files
clean-temps:
    rm -rf .mypy_cache/ .ruff_cache/ cz_plugin_espressif/cz_plugin_espressif.egg-info

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
