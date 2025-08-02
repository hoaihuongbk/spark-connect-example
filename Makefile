.PHONY: venv build run create-job

venv:
	uv venv

build: venv
	uv pip install .

run: build
	uv run spark_connect_example.py

create-job:
	databricks jobs create --json @databricks-job.json 