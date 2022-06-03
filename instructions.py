#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: This module contains the instructions for 
    installing and managing the project with python poetry.
Autor: Prabal Pathak


install: poetry 
Url: https://python-poetry.org/
Linux:
1. pip3 install -U poetry or 
2. curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

Windows:
1. pip install -U poetry or
2. (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -


Uses:
1. create a new project with poetry
command: poetry new --name <project-name>
or 
command: poetry new --name <project-name> --src <project-path>

2. activate the environment
command: poetry shell

3. Add dependencies to the project
command: poetry add <package-name>

or 
install from poetry.lock or pyproject.toml or update lock file.
command: poetry install

4. If you want to change the env python version, you can use the following command:
command: poetry env use <python-version>

5. Lock the dependencies
command: poetry lock

6. Build installable package
command: poetry build


--------------------------------- ------------------------------------- UNIT TESTING ---------------------------------------------------
command: python3 -m unittest discover 
"""

