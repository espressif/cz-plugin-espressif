# This Justfile contains rules/targets/scripts/commands that are used when
# developing. Unlike a Makefile, running `just <cmd>` will always invoke
# that command. For more information, see https://github.com/casey/just

# This setting will allow passing arguments through to recipes
set positional-arguments

# Parse current version from pyproject.toml
current_version := `grep -Po 'version\s*=\s*"\K[^"]*' pyproject.toml | grep -Eo '[0-9]+\.[0-9]+\.[0-9]+'`

# Custom git log format
gitstyle := '%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'


# Helper function for quick menu
[private]
@default:
    just --list


# ... Edit this Justfile
@edit-just:
    $EDITOR ./Justfile


# PROJECT: Release version info and list of commits since last release
@version:
    cz bump --dry-run | grep -E 'change\(bump\)|tag to create|increment detected'; \
    echo "\nCommits since last release:"; \
    git log -n 30 --graph --pretty="{{gitstyle}}" v{{current_version}}..HEAD


# PROJECT: Install development environment
@install:
    pip install --require-virtualenv -e '.[dev,test]'
    pip install --require-virtualenv --upgrade pip


# PROJECT: Re-compile requirements.txt from dev-dependencies in pyproject.toml
@lock-requirements:
    pip-compile --strip-extras --output-file=requirements.txt pyproject.toml > /dev/null


# PROJECT: Remove caches, builds, reports and other generated files
@clean:
    rm -rf \
        .coverage \
        .coverage.* \
        .mypy_cache \
        .pytest_cache \
        .ruff_cache \
        *.egg-info \
        **/__pycache__/ \
        build \
        **/__pycache__/ \
        **/*.test.md \
        build \
        demo \
        dist \
        :


# PROJECT: Build and check distribution package
@build:
    just clean
    python -m build
    twine check dist/*


# PROJECT:
@bump-test:
    clear
    pre-commit run --all-files
    cz bump --dry-run


# PYTEST: Run tests with coverage report
@test:
    pytest

# PYTEST: Updade snapshots (known results) for pytest
@update-snapshots:
    pytest --snapshot-update


# DOCKER: Test Build Docker image for demo
@docker-test-buildx:
    cd docker && docker buildx build --platform linux/arm64,linux/amd64 -t tomasad/czespressif-demo . && cd -


# DOCKER: Build and push Docker image for demo
@docker-push-buildx:
    cd docker && docker buildx build --platform linux/arm64,linux/amd64 -t tomasad/czespressif-demo --push . && cd -


# DOCKER: Run Docker image for demo
@docker-run directory=".":
    pushd {{directory}} && docker run --rm -v $(pwd):/app -u $(id -u):$(id -g) tomasad/czespressif-demo && popd


# GIT: Show commits only on current branch
@branch-commits base="master":
    @if git rev-parse --verify "{{base}}" > /dev/null 2>&1; then \
        git log --first-parent --no-merges --graph --pretty="{{gitstyle}}" {{base}}..HEAD; \
    else \
        echo 'E: Provide base (target) branch as argument to `just branch-commits <base-branch>`' >&2; \
        exit 128; \
    fi


# GIT: Try commit again, open failed commit message it in the editor for corrections
@recommit:
    git commit --edit --file=$(git rev-parse --git-dir)/COMMIT_EDITMSG


# GIT: Run interactive "git rebase" command
@rebase base="master":
    git fetch origin {{base}}
    git rebase -i origin/{{base}}


# ----------------------------------------------

@generate-cz-bump:
    clear
    cz bump --dry-run | tee "output/cz-bump.test.md"


@generate-cz-example:
    clear
    cz example | tee "output/cz-example.test.md"


@generate-cz-info:
    clear
    cz info | tee "output/cz-info.test.md"


@generate-cz-schema:
    clear
    cz schema | tee "output/cz-schema.test.md"


@generate-changelog:
    clear
    cz changelog --dry-run | tee "output/CHANGELOG.test.md"


@generate-changelog-incremental:
    clear
    cz changelog --incremental --dry-run | tee "output/CHANGELOG-incremental.test.md"


@generate-release-notes:
    clear
    cz changelog v1.1.0 --template="RELEASE_NOTES.md.j2" --dry-run | tee "output/RELEASE_NOTES.test.md"
