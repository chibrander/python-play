import pandas as pd
#import pymysql.cursors
from sqlalchemy import create_engine

uname = 'root'
upass = 'root'
uhost= 'localhost:3306'
udb = 'raymond'
usocket = '&unix_socket=/Applications/MAMP/tmp/mysql/mysql.sock'

sql_alch_con = 'mysql+pymysql://' + uname + ':' + upass + '@' + uhost + '/' + udb + '?charset=utf8' + usocket

engine = create_engine(sql_alch_con, echo=False)
