import psycopg2

from psycopg2 import sql

import os

DB_URL = os.environ.get("DATABASE_URL", "dbname=allie_db")



def sql_select(query):
  conn = psycopg2.connect(DB_URL)
  cur = conn.cursor()
  cur.execute(query)
  results = cur.fetchall()
  cur.close()
  conn.close()
  return results

def sql_write(query, params):
  conn = psycopg2.connect(DB_URL)
  cur = conn.cursor()
  cur.execute(query, params)
  conn.commit()
  conn.close()

def sql_select_wright(query, params):
  conn = psycopg2.connect(DB_URL)
  cur = conn.cursor()
  cur.execute(query, params)
  results = cur.fetchall()
  cur.close()
  conn.close()
  return results  