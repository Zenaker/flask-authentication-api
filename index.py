from flask import Flask, request, jsonify
from database.db_parser import *


app = Flask(__name__)

@app.route("/auth/register", methods=['POST'])
def register_user():

    username, email, password = request.values['username'], request.values['email'], request.values['password']
    result = register(username, email, password)

    if result == True:
        return jsonify({"status":"success"}), 200

    return jsonify({"error":result}), 404


@app.route("/auth/login", methods=['POST'])
def login_user():
    email, password = request.values['email'], request.values['password']
    logged_in = login(email, password)

    if logged_in == "OK":
        return jsonify({"status":"success"}), 200
    
    return jsonify({"error":logged_in}), 404


@app.route("/", methods=['GET'])
def index():
    return "yes"

if __name__ == '__main__':
    app.run()
