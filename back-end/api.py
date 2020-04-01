from flask import Flask, jsonify
from flask_restful import Resource, Api
from typing import List, Dict
import mysql.connector
import json

app = Flask(__name__)

api = Api(app)

connection = mysql.connector.connect(
  host="addressofyourdatabase",
  user="username",
  passwd="password",
  database="database name"
)

cursor = connection.cursor()
cursor.execute("select * from customers")
row_headers=[x[0] for x in cursor.description]
myresult = cursor.fetchall()
json_data=[]
for result in myresult:
     json_data.append(dict(zip(row_headers,result)))
connection.close()

class Product(Resource):
	def get(self):
		return jsonify(json_data)

api.add_resource(Product,'/')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80, debug=True)
