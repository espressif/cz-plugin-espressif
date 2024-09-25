#!/bin/bash

# Check if the .git directory exists in the current directory
if [ ! -d ".git" ]; then
    echo "Error: This script must be run in a directory where a .git directory is present."
    exit 1
fi

# Variables
DEMO_DIR="demo"
BACKUP_DIR="/tmp/czespressif-backup"
ORIGINAL_PYPROJECT="pyproject.toml"
BACKUP_PYPROJECT="$BACKUP_DIR/pyproject.toml"
DEMO_CHANGELOG="$DEMO_DIR/CHANGELOG.md"
DEMO_RELEASE_NOTES="$DEMO_DIR/RELEASE_NOTES.md"
DEMO_CHANGELOG_NO_EMOJIS="$DEMO_DIR/CHANGELOG-no-emojis.md"
DEMO_RELEASE_NOTES_NO_EMOJIS="$DEMO_DIR/RELEASE_NOTES-no-emojis.md"
DEMO_CHANGELOG_ALL_TYPES="$DEMO_DIR/CHANGELOG-all-types.md"
DEMO_RELEASE_NOTES_ALL_TYPES="$DEMO_DIR/RELEASE_NOTES-all-types.md"

# Remove demo directory and backup directory if they exist
rm -rf $DEMO_DIR $BACKUP_DIR

# Check if pyproject.toml exists before backing it up
backup_exists=false
if [ -f "$ORIGINAL_PYPROJECT" ]; then
    # Create backup of the original pyproject.toml
    echo "Creating backup of current pyproject.toml ..."
    mkdir -p $BACKUP_DIR
    mv $ORIGINAL_PYPROJECT $BACKUP_PYPROJECT
    backup_exists=true
else
    echo "Config pyproject.toml not found, skipping backup ..."
fi

# Rewrite the pyproject.toml to use the local version of the plugin
echo "Creating temporary pyproject.toml config for running demo ..."

cat <<EOL >$ORIGINAL_PYPROJECT
[tool.commitizen]
name = "czespressif"
bump_message = 'change(bump): release \$current_version → \$new_version [skip-ci]'
changelog_merge_prerelease = true
tag_format = "v\$version"
EOL

# Create subdirectory for the demo outputs
mkdir -p $DEMO_DIR

# 1- DEFAULT SETTINGS RUN
echo "Creating demo examples with default config ..."

# Run Commitizen commands (default settings)
cz changelog --file-name="$DEMO_CHANGELOG"
cz changelog --incremental --template="RELEASE_NOTES.md.j2" --file-name="$DEMO_RELEASE_NOTES"

# 3 - NO EMOJIS SETTINGS RUN
echo "Creating demo examples without using emojis ..."

# Disable emojis and update pyproject.toml
echo "use_emoji = false" >>$ORIGINAL_PYPROJECT
sleep 2

# Run Commitizen commands (no emojis settings)
cz changelog --file-name="$DEMO_CHANGELOG_NO_EMOJIS"
cz changelog --incremental --template="RELEASE_NOTES.md.j2" --file-name="$DEMO_RELEASE_NOTES_NO_EMOJIS"

# 3 - ALL TYPES IN CHANGELOG
echo "Creating demo examples withall types in changelog ..."

# Add all types to the changelog and update pyproject.toml
sed -i '/use_emoji = false/d' $ORIGINAL_PYPROJECT
echo "types_in_changelog = ['BREAKING CHANGE','feat','fix','docs','refactor','remove','change','ci','test','revert']" >>$ORIGINAL_PYPROJECT
sleep 2

# Run Commitizen commands (all types settings)
cz changelog --file-name="$DEMO_CHANGELOG_ALL_TYPES"
cz changelog --incremental --template="RELEASE_NOTES.md.j2" --file-name="$DEMO_RELEASE_NOTES_ALL_TYPES"

# Restore the original pyproject.toml if it was backed up
if [ "$backup_exists" = true ]; then
    echo "Restoring backup ..."
    rm $ORIGINAL_PYPROJECT
    mv $BACKUP_PYPROJECT $ORIGINAL_PYPROJECT
else
    # If no backup exists, clean up the generated pyproject.toml
    echo "Cleaning ..."
    rm $ORIGINAL_PYPROJECT
fi

# Change ownership of the generated files to the user running the container
chown -R $(id -u):$(id -g) $DEMO_DIR

# Change ownership of the restored pyproject.toml if it was restored
if [ "$backup_exists" = true ]; then
    chown $(id -u):$(id -g) $ORIGINAL_PYPROJECT
fi

echo -e "\n\033[0;32mDONE: Check subdirectory 'demo' in your project with generated examples!\033[0m"
