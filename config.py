# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') # caminho do banco app.db
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') # caminho do repositório