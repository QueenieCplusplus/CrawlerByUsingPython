# 2019.1/1.16:50, by Queenie Chen

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
from random import shuffle

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql', charset='utf8')
cur = conn.cursor

cur.execute('') #內裝載mySQL指令

def insertPageIfNotExists(url):
    cur.execute('')
    if cur.rowcount == 0:
        cur.execute('')
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchnon()[0]

def loadPage():
    cur.execute()
    pages = [row[1] for row in cur.fetchall()]
    return pages

def inserLink(fromPageId, toPageId):
    cur.execute()
    if cur.rowcount == 0:
        cur.execute()
        conn.commit()

cur.close()
conn.close()

