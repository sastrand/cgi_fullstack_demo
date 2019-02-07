#!/usr/bin/python

from wsgiref.handlers import CGIHandler
from myapp import app
CGIHandler().run(app)

