
from fastapi import Request

def get_current_user(request: Request):
    return "{{cookiecutter.repo_name}}"
