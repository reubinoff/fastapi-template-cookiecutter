#!/bin/bash

poetry install
poetry update
poetry env use 3.8
use nox -rs pre-commit