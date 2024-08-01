

username_password_dict = {
    'Apt1030': 'password123',
    'user1': 'admin123',
    'user2': 'user123'
}

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in username_password_dict:
        if username_password_dict[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password!")
    else:
        print("Username not found!")
    if not username or not password:
        print('Username and password cannot be empty')

    if len(password) < 8:
        print('Password must be at least 8 characters long')


if __name__ == "__main__":
    login()