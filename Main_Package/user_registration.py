# user_registration.py

import json
import bcrypt

def register_user(username, password):
    # Load existing user data from JSON file
    try:
        with open('user_data.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    # Check if the username is already taken
    if username in users:
        print("Username already exists. Please choose a different one.")
        return

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Save user data to JSON file
    users[username] = {'hashed_password': hashed_password.decode('utf-8')}
    with open('user_data.json', 'w') as file:
        json.dump(users, file)

    print("Registration successful.")

def login_user(username, password):
    # Load user data from JSON file
    try:
        with open('user_data.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        print("No users registered yet.")
        return

    # Check if the username exists
    if username not in users:
        print("Username not found.")
        return

    # Retrieve hashed password
    stored_hashed_password = users[username]['hashed_password']

    # Verify the entered password
    if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
        print("Login successful.")
    else:
        print("Incorrect password.")

# Example usage:
register_user('john_doe', 'secure_password')
login_user('john_doe', 'secure_password')
