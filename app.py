from flask import Flask, request, jsonify
from models import create_user, get_users
import requests
import os

print("Current working directory:", os.getcwd())
app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user_route():
    data = request.json
    create_user(data['name'], data['email'])
    return jsonify({"message": "User created successfully"})

@app.route('/get_users', methods=['GET'])
def get_users_route():
    users = get_users()
    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(debug=True)

FLASK_ENDPOINT = "http://localhost:5000"  # Adjust the endpoint based on your Flask setup

def create_user_in_db(name, email):
    data = {"name": name, "email": email}
    response = requests.post(f"{FLASK_ENDPOINT}/create_user", json=data)
    return response.json()

def get_users_from_db():
    response = requests.get(f"{FLASK_ENDPOINT}/get_users")
    return response.json()["users"]
