import configparser
import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()

path = os.path.join(os.getcwd(), 'database', 'sql_config.ini')
config.read(path)

host = config['mysql']['host']
user = config['mysql']['user']
password = config['mysql']['password']

DATABASE_URL = f'mysql+mysqlconnector://{user}:{password}@{host}/peripheral?auth_plugin=mysql_native_password'

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()

# 导入datamodel中的数据表模型创建数据库
from . import datamodel
datamodel.Base.metadata.create_all(engine)
