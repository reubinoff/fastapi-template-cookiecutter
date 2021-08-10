# -*- coding: utf-8 -*-
import logging

import uvicorn

if __name__ == "__main__":
    uvicorn.run("{{cookiecutter.repo_name}}.main:app", host="0.0.0.0", log_level=logging.DEBUG)
