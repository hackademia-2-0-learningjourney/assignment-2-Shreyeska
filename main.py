#import necessary files
import json
import os

# Create a user.json file in the same directory as the main.py file
data_file = 'user.json'

# Function to load user data from the JSON file
def load_data():
    if not os.path.exists(data_file):
        return {}
    try:
        with open(data_file, 'r') as file:#r is for reading the file
            return json.load(file)
    except json.JSONDecodeError:
        return {}

# Function to save user data to the JSON file
def save_data(data):
    #write the data to the file
    with open(data_file, 'w') as file: 
        json.dump(data, file, indent=4)

# Function for signing up a new user
def sign_up():
    data = load_data()
    username = input("Enter username: ")
    if username in data:
        print("Username already exists. Try a different username.")
        return
    password = input("Enter password: ")
    phone_number = input("Enter phone number: ")
    
    data[username] = {
        'password': password,
        'phone_number': phone_number
    }
    save_data(data)
    print("Sign up successful!")

# Function for signing in an existing user
def sign_in():
    data = load_data()
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in data and data[username]['password'] == password:
        print(f"Welcome to the device, {username}!")
        print(f"Your phone number is {data[username]['phone_number']}")
    else:
        print("Incorrect credentials. Program terminated.")

# Main function to display the menu and take user input
def main():
    while True:
        print("\n1. Sign up")
        print("2. Sign in")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            sign_up()
        elif choice == '2':
            sign_in()
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
