set quiet := true
set positional-arguments := true

[private]
@default:
    just --list

exit:
    exit 0

# ... Edit this Justfile
@edit-just:
    $EDITOR ./Justfile

build-install:
    pip uninstall -y czespressif
    python -m build
    pip install .
    cz example
    just get-versions

# PROJECT: Release version info and list of commits since last release
@version:
    cz bump --dry-run | grep -E 'change\(bump\)|tag to create|increment detected'; \
    echo "\nCommits since last release:"; \
    git log -n 30 --graph --pretty="{{gitstyle}}" v{{current_version}}..HEAD

release-notes-show:
    cz changelog v1.0.0 --template="RELEASE_NOTES.md.j2" --dry-run

# PROJECT: Install development environment
@install:
    pip install --require-virtualenv -e '.[dev,test]'
    pip install --require-virtualenv --upgrade pip


# PROJECT: Re-compile requirements.txt from dev-dependencies in pyproject.toml
@lock-requirements:
    pip-compile --strip-extras --output-file=requirements.txt pyproject.toml > /dev/null

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
        **/__pycache__/ \
        build \
        **/__pycache__/ \
        demo \
        dist \
        :

docker-build:
    cd docker && docker build -t tomasad/czespressif-demo . && cd -

# PROJECT: Build and check distribution package
@build:
    just clean
    python -m build
    twine check dist/*

docker-run:
    docker run --rm -v $(pwd):/app -u $(id -u):$(id -g) tomasad/czespressif-demo

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
