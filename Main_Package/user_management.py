# user_management.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, entered_password):
        return self.password == entered_password