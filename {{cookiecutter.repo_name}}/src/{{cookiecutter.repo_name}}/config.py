# -*- coding: utf-8 -*-
import os

from pydantic import BaseModel
from pydantic import BaseSettings
from pydantic import Field


class SettingOfSomeModel(BaseModel):
    foo: str = Field(default="asasd", env="my_foo_value")
    apple = 1


class Configuration(BaseSettings):
    log_level: str = "DEBUG"
    env: str = "local"

    sentry_dsn: str = ""
    app_name: str = "Awesome Project"
    admin_email: str
    some_model: SettingOfSomeModel = SettingOfSomeModel()

    db_name = "{{cookiecutter.repo_name}}"
    db_pass = "sql"
    db_host = "localhost"

    alembix_ini = (f"{os.path.dirname(os.path.realpath(__file__))}/alembic.ini",)

    class Config:
        env_file = ".env"


configuration = Configuration()
