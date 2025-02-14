# User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:
# Welcome to the Contact Management System! 
# Menu:
# 1. Add a new contact
# 2. Edit an existing contact
# 3. Delete a contact
# 4. Search for a contact
# 5. Display all contacts
# 6. Export contacts to a text file
# 7. Import contacts from a text file *BONUS*
# 8. Quit

import re
from tabulate import tabulate
import os

Menu = (
    ["1. Add a new contact"],
    ["2. Edit an existing contact"],
    ["3. Delete a contact"],
    ["4. Search for a contact"],
    ["5. Display all contacts"],
    ["6. Export contacts to a text file"],
    ["7. Import contacts from a text file *BONUS*"],
    ["8. Quit"])
print(tabulate(Menu, headers=["Welcome to the Contact Managment System!"], tablefmt="grid"))
# Contact Data Storage:
# Use nested dictionaries as the main data structure for storing contact information.
# Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
# Store contact details within the inner dictionary, including:
# Name
# Phone number
# Email address
# Additional information (e.g., address, notes).
# Menu Actions:
# Implement the following actions in response to menu selections:
# Adding a new contact.

def validate_phone(phone):
    #check phone number
    pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    while not re.match(pattern, phone):
        print(" Invalid phone. Try again.")
        phone = input("Phone Number:").strip()
    return phone

def validate_email(email):
    #check email
    while not re.match(pattern, email):
        print("Invalid email. Try again.")
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    email = input("Email Address:").strip()
    return email

def validate_zip(zip_code):
    #Check Zip Code
    while not re.match(pattern, zip_code):
        print("Invalid Zip Code. Try again:")
    pattern = r"^\d{5}(-\d{4})?$"
    zip_code = input("Zip Code:").strip()
    return zip_code
    

def new_contact():

    new_user = input("Full Name: ").strip()
    phone_number = validate_phone(input("Phone Number: ").strip())
    email_address = validate_email(input("Email Address: ").strip())

    street_address = input("Street Address: ").strip()
    apt_number = input("Apt #: ").strip()
    city = input("City: ").strip()
    state = input("State: ").strip()
    country = input("Country: ").strip()
    zip_code = validate_zip(input("ZIP Code: ").strip())

    #  Address
    home_address = f"{street_address}, Apt {apt_number}, {city}, {state}, {country}, ZIP: {zip_code}"
    print("\n Contact Successfully Added!")
    print(f" Name: {new_user}")
    print(f" Phone: {phone_number}")
    print(f"Email: {email_address}")
    print(f"Address: {home_address}")

    if new_contact and home_address:
        contact_list.append(new_user,home_address)

contact_list = []

def display_list():
    print(tabulate(contact_list, headers=["Full Name", "Phone", "Email Address", "Address"],tablefmt="grid"))



display_list()

# Editing an existing contact's information (name, phone number, email, etc.).
# Deleting a contact.
# Searching for a contact and displaying their details.
# Displaying a list of all contacts.
# Exporting contacts to a text file in a structured format.
# Importing contacts from a text file and adding them to the system. * BONUS
# User Interaction:
# Utilize input() to enable users to select menu options and provide contact details.
# Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.
# Error Handling:
# Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.
# GitHub Repository:
# Create a GitHub repository for your project.
# Create a clean and interactive README.md file in your GitHub repository.
# Include clear instructions on how to run the application and explanations of its features.
# NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

# The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

#View Rubric here: Module 3 Mini Project Rubric