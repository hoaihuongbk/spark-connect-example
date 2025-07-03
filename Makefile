.PHONY: venv build run

venv:
	uv venv

build: venv
	uv pip install .

run: build
	uv run spark_connect_example.py 