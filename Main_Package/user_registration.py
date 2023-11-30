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
    if username.lower in users:
        print("Username already exists. Please choose a different one.")
        return False

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Save user data to JSON file
    users[username] = {'hashed_password': hashed_password.decode('utf-8')}
    with open('user_data.json', 'w') as file:
        json.dump(users, file)

    return True


def login_user(username, password):
    # Load user data from JSON file
    try:
        with open('user_data.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        print("No users registered yet, please register to continue")
        return False

    # Check if the username exists
    if username not in users:
        print("Username not found, please try again or register to continue")
        return False

    # Retrieve hashed password
    stored_hashed_password = users[username]['hashed_password']

    counter = 3
    while counter > 0:
        # Verify the entered password
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
            return True
        else:
            print(f"Incorrect password,{counter} attempts left, try again")
            counter -= 1
            password = input("Enter your password: ")

    return False
