#!/usr/bin/env python3

import datetime
import environment as env
from tornado.log import app_log
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Downloads(Base):
    __tablename__ = 'downloads'

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    date  = Column(DateTime)

class DB(object, metaclass=Singleton):
    def __init__(self):
        self.pool = create_engine(
                  'postgresql://{uname}:{pwd}@{container}:5432/{db}'
                  .format(uname=env.db_user,
                          pwd=env.db_pwd,
                          container=env.db_ip,
                          db=env.db_dbname),
                  pool_size=20,
                  max_overflow=10
                 )
        
        Base.metadata.create_all(self.pool)

    def connection(self):

        # test the connection
        conn = self.pool.connect()
        return conn

    def insert(self, username):
        app_log.info(f'Inserting into database: {username}')


        Session = sessionmaker(bind=self.pool)
        session = Session()

        data = Downloads(username=username,
                         date=datetime.datetime.now())
        session.add(data)
        session.commit()



def test():
    import json
    data = {'name': 'test', 'att': 1}
    jdata = json.dumps(data)


    import pdb; pdb.set_trace()
    d = MatlabDB()
#    d.insert_instance(jdata)
    print('done')

    query = "data->>'name' = 'test'"
    d.get_instances_by_json_query(query)

