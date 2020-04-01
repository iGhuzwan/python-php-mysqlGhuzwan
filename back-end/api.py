from flask import Flask
from flask_restful import Resource, Api
from typing import List, Dict
import mysql.connector
import json

app = Flask(__name__)

api = Api(app)

connection = mysql.connector.connect(
  host="ghuzwandb.cxa0uufajue5.us-east-1.rds.amazonaws.com",
  user="admin",
  passwd="laly7792420",
  database="cloud"
)

cursor = connection.cursor()
cursor.execute("select * from customers")
myresult = cursor.fetchall()
connection.close()

class Product(Resource):
	def get(self):
		return myresult 

api.add_resource(Product,'/')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80, debug=True)
