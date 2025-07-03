# Spark Connect Example with Databricks Serverless

## Overview

This repository demonstrates how to use [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/index.html) to connect your local Python environment to a Databricks serverless SQL warehouse or cluster. It provides a ready-to-run example that creates a DataFrame, writes it to a Databricks table, runs a SQL query, and cleans up—all from your local machine.

## Prerequisites

- **Python 3.10 or newer**
- Access to a Databricks workspace (with serverless SQL warehouse or cluster)
- [Make](https://www.gnu.org/software/make/) installed (for using the Makefile)
- [Databricks CLI v0.205+](https://docs.databricks.com/en/dev-tools/cli/index.html) installed locally

## Setup

1. **Clone this repository:**
   ```sh
   git clone <this-repo-url>
   cd spark-connect-example
   ```

2. **Create a virtual environment and install dependencies:**
   ```sh
   make venv
   ```

3. **(Optional) Rebuild dependencies:**
   ```sh
   make build
   ```

## Authentication

1. **Set up Databricks CLI authentication (OAuth recommended):**
   ```sh
   bash setup_databricks_profile.sh
   ```
   This will open a browser for you to log in and select your workspace and cluster/serverless SQL warehouse. The CLI will save your credentials in a local profile.

2. **(Optional) Select a specific profile:**
   - By default, the example uses the `DEFAULT` profile. To use another, edit the Python script to use:
     ```python
     spark = DatabricksSession.builder.profile("<profile-name>").serverless().getOrCreate()
     ```

## Running the Example

1. **Start your Databricks cluster or serverless SQL warehouse.**
2. **Run the example script:**
   ```sh
   make run
   ```

You will see step-by-step output with icons explaining each stage:
- Connecting to Databricks
- Creating and showing a DataFrame
- Writing to a Databricks table
- Querying and displaying results
- Cleaning up the table

## Troubleshooting
- Ensure your Python version is >= 3.10.
- Make sure your Databricks CLI is authenticated and points to a running cluster or serverless SQL warehouse.
- If you see import errors for `databricks.connect`, check that `databricks-connect` is installed in your environment.
- For more details, see the [official Databricks Connect Python examples](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/examples).

## References
- [Databricks Connect for Python: Official Docs & Examples](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/examples)
- [Databricks CLI Authentication](https://docs.databricks.com/en/dev-tools/cli/authentication.html) 