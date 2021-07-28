#!/bin/bash

poetry install
poetry update
poetry env use 3.8
poetry shell
nox --session=pre-commit -- install
nox -r --session=pre-commit -- run --all-files
