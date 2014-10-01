#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Flask
SECRET_KEY = os.urandom(32)

# SQLAlchemy (DB)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://localhost/downstream'  # NOQA

FILES_PATH = 'tmp/'
TAGS_PATH = 'tags/'
