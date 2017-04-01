#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

Base = declarative_base()

class Proxy(Base):
    __tablename__ = 'proxy'
    id = Column(Integer, primary_key=True)
    ip = Column(String)
    port = Column(String)


engine = create_engine('sqlite:///sqlalchemy_db.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

with open('proxies.json') as proxies:
    obj = json.loads(proxies.read())
    for i in range(len(obj)):
        proxy = Proxy(ip = obj[i]['ip'],
                      port = obj[i]['port'])
        session.add(proxy)
session.commit()
