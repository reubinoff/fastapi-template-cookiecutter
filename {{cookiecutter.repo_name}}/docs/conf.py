# -*- coding: utf-8 -*-
"""Sphinx configuration."""
from datetime import datetime


project = "template_name"
author = "OwnBackup"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_click", "sphinx_rtd_theme"]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
