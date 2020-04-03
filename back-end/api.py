from flask import Flask, jsonify
from flask_restful import Resource, Api
from typing import List, Dict
import mysql.connector
import mariadb
import psycopg2
import sys
import json

app = Flask(__name__)

api = Api(app)

postgreConn = psycopg2.connect(host="cluddbpostgresql.cxa0uufajue5.us-east-1.rds.amazonaws.com",database="ghuzwandb", user="postgres", password="laly7792420")
postgreConn.autocommit = True

postgreCur = postgreConn.cursor()

postgreCur.execute("SELECT id, name, address, salary  from COMPANY")
row_headersPostgre=[x[0] for x in postgreCur.description]
myresultpostgre = postgreCur.fetchall()
json_dataPostgre=[]
for result in myresultpostgre:
     json_dataPostgre.append(dict(zip(row_headersPostgre,result)))
postgreConn.close()

# Instantiate Connection
try:
   mariadbConn = mariadb.connect(
      user="admin",
      password="laly7792420",
      host="clouddbmaria.cxa0uufajue5.us-east-1.rds.amazonaws.com",
      port=3306,
      database="ghuzwandb"
	)
except mariadb.Error as e:
    print("Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Instantiate Cursor
cur = mariadbConn.cursor()
cur.execute("Select * from customers")

row_headersMariaDB=[x[0] for x in cur.description]
myresult = cur.fetchall()
json_dataMaraiDB=[]
for result in myresult:
     json_dataMaraiDB.append(dict(zip(row_headersMariaDB,result)))
mariadbConn.close()

# MySQL Connection
'''connection = mysql.connector.connect(
  host="ghuzwandb.cxa0uufajue5.us-east-1.rds.amazonaws.com",
  user="admin",
  passwd="laly7792420",
  database="ghuzwandb"
)

cursor = connection.cursor()
cursor.execute("select * from customers")
row_headers=[x[0] for x in cursor.description]
myresult = cursor.fetchall()
json_data=[]
for result in myresult:
     json_data.append(dict(zip(row_headers,result)))
connection.close()

class MysqlDB(Resource):
	def get(self):
		return jsonify(json_data)
'''
class MariaDB(Resource):
	def get(self):
		return jsonify(json_dataMaraiDB)

class Postgres(Resource):
	def get(self):
		return jsonify(json_dataPostgre)


api.add_resource(Postgres,'/')
api.add_resource(MariaDB,'/mariadb')
#api.add_resource(MysqlDB,'/mysqldb')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80, debug=True)
