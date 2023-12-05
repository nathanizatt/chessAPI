import flask
from flask import request, jsonify
from flask import Flask, render_template, request
from config import *
import pymysql.cursors
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])

def index():
    return render_template('index.html')

@app.route('/eco-finder', methods=['GET'])

def eco():
    return render_template('eco.html')

@app.route('/eco-finder/eco', methods=['GET'])

def eco_id():
    if 'eco' in request.args:
        eco = str(request.args['eco'])
    else:
        return "Error: No ECO provided. Please specify a ECO."
# Initiate RDS connection
    connection = start_rds_connection()
    with connection.cursor() as cursor:
        sql = f"SELECT ECO, opening_name, num_games, perc_white_win, perc_black_win FROM high_elo_opening WHERE ECO = '{eco}';"
        cursor.execute(sql)
        result = cursor.fetchall() # Retrieve all rows
        #connection.commit()
    connection.close()
    response = jsonify(result)
    response.data = json.dumps(response.json, indent=2)
    return response

@app.route('/list', methods=['GET'])

def list():
    connection = start_rds_connection()
    with connection.cursor() as cursor:
        sql = f"SELECT ECO, opening_name FROM high_elo_opening;"
        cursor.execute(sql)
        result = cursor.fetchall() # Retrieve all rows
        #connection.commit()
    connection.close()
    response = jsonify(result)
    response.data = json.dumps(response.json, indent=2)
    return response

# Define function to establish RDS connection
def start_rds_connection():
    try:
        connection = pymysql.connect(host=ENDPOINT,
        port=PORT,
        user=USERNAME,
        passwd=PASSWORD,
        db=DBNAME,
        cursorclass=CURSORCLASS,
        ssl_ca=SSL_CA)
        print('[+] RDS Connection Successful')
    except Exception as e:
        print(f'[+] RDS Connection Failed: {e}')
        connection = None

    return connection
