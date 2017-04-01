#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy_database import Proxy, Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sqlalchemy_db.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

proxy = session.query(Proxy).first()

print proxy.id, proxy.ip, proxy.port

