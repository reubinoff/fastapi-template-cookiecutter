#!/bin/bash

poetry install
poetry update
poetry env use 3.8
poetry run nox -rs pre-commit