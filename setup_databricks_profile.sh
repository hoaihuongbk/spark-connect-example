#!/bin/bash

# Script to set up Databricks CLI profile using OAuth (browser-based login)
# Usage: bash setup_databricks_profile.sh

set -e

# Check if databricks CLI is installed, install if not
if ! command -v databricks &> /dev/null; then
    echo "databricks CLI not found. Installing..."
    pip install --user databricks-cli
    export PATH="$HOME/.local/bin:$PATH"
fi

echo "Enter a name for your Databricks CLI profile (default: 'DEFAULT'):"
read -r PROFILE_NAME
PROFILE_NAME=${PROFILE_NAME:-DEFAULT}

echo "Enter your Databricks workspace URL (e.g. https://<region>.cloud.databricks.com):"
read -r DATABRICKS_HOST

# Use OAuth login, which will open a browser for authentication

echo "Launching browser for OAuth login..."
databricks auth login --host "$DATABRICKS_HOST" --profile "$PROFILE_NAME"

echo "Profile '$PROFILE_NAME' configured successfully with OAuth!" 