# coding: utf-8
from __future__ import unicode_literals

from fabric.api import *

from fabtools import require
from fabtools import python
from fabtools.vagrant import vagrant


VENV_PATH = 'venv'


@task
def build_env():
    require.python.virtualenv(VENV_PATH)
    with python.virtualenv(VENV_PATH):
        require.python.requirements('/vagrant/requirements/local.txt')

