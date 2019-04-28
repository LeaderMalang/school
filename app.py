#!/usr/bin/env python3

# import the nessecary pieces from Flask

from flask import Flask,render_template, request,jsonify,Response
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

#Create the app object that will route our calls

app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'sms'
# mysql = MySQL(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sms'
db = SQLAlchemy(app)



# Add a single endpoint that we can use for testing

@app.route('/', methods = ['GET'])
def home():
    return render_template("index.html")

#When run from command line, start the server
if __name__ == '__main__':
    print(db)
    app.run( debug = True)