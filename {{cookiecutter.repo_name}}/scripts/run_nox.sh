#!/bin/bash

poetry install
poetry update
poetry env use 3.8
nox -rs pre-commit