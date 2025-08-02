.PHONY: venv build run dbt-deps dbt-seed dbt-run

venv:
	uv venv

build: venv
	uv pip install .

run: build
	uv run spark_connect_example.py

dbt-deps:
	uv run dbt deps --project-dir dbt_spark_connect_example --profiles-dir dbt_spark_connect_example/profiles

dbt-seed:
	uv run dbt seed --project-dir dbt_spark_connect_example --profiles-dir dbt_spark_connect_example/profiles

dbt-run:
	uv run dbt run --project-dir dbt_spark_connect_example --profiles-dir dbt_spark_connect_example/profiles 