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

import re
import os
from tabulate import tabulate

# Star Wars Themed Welcome Message
print("\n*** Jedi Archives Terminal ***")
print("[Accessing Galactic Holonet Database...]")
print("Welcome, Commander Skywalker. What would you like to do?")

# Contact Storage
contacts = {}
file_name = "archives.txt"

# Load contacts if the file exists
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        for line in f:
            name, phone, email, address = line.strip().split(", ")
            contacts[name] = {"Phone": phone, "Email": email, "Address": address}

# Validation Functions
def validate_phone(phone):
    pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    while not re.match(pattern, phone):
        print("[ERROR] Invalid frequency code. Try again.")
        phone = input("Comlink Frequency: ").strip()
    return phone

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    while not re.match(pattern, email):
        print("[ERROR] Invalid holonet address. Try again.")
        email = input("Holonet Address: ").strip()
    return email

def validate_zip(zip_code):
    pattern = r"^\d{5}(-\d{4})?$"
    while not re.match(pattern, zip_code):
        print("[ERROR] Invalid sector code. Try again.")
        zip_code = input("Sector Code: ").strip()
    return zip_code

# Functions for Contact Management
def add_contact():
    name = input("Jedi or Rebel Name: ").strip()
    phone = validate_phone(input("Comlink Frequency: ").strip())
    email = validate_email(input("Holonet Address: ").strip())
    address = input("Last Known Location: ").strip()
    
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    save_contacts()
    print(f"[CONFIRMED] {name} has been added to the Jedi Archives.")

def edit_contact():
    name = input("Enter the name of the contact to edit: ").strip()
    if name in contacts:
        print("Leave blank to keep current record.")
        phone = input(f"New Comlink Frequency ({contacts[name]['Phone']}): ").strip() or contacts[name]['Phone']
        email = input(f"New Holonet Address ({contacts[name]['Email']}): ").strip() or contacts[name]['Email']
        address = input(f"New Last Known Location ({contacts[name]['Address']}): ").strip() or contacts[name]['Address']
        
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        print(f"[CONFIRMED] {name}'s records have been updated!")
    else:
        print("[ERROR] That record does not exist in the Jedi Archives.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"[ALERT] {name} has been removed from the Jedi Archives.")
    else:
        print("[ERROR] That name does not exist in the Jedi Archives.")

def search_contact():
    name = input("Enter the name to search for: ").strip()
    if name in contacts:
        print(tabulate([[name, contacts[name]['Phone'], contacts[name]['Email'], contacts[name]['Address']]],
                       headers=["Name", "Comlink Frequency", "Holonet Address", "Last Known Location"], tablefmt="grid"))
    else:
        print("[ERROR] No record found in the Jedi Archives.")

def display_contacts():
    if contacts:
        table = [[name, info['Phone'], info['Email'], info['Address']] for name, info in contacts.items()]
        print(tabulate(table, headers=["Name", "Comlink Frequency", "Holonet Address", "Last Known Location"], tablefmt="grid"))
    else:
        print("[ALERT] The Jedi Archives are empty.")

def export_contacts():
    with open("archives.txt", "w") as f:
        for name, info in contacts.items():
            f.write(f"{name}, {info['Phone']}, {info['Email']}, {info['Address']}\n")
    print("[SUCCESS] Records exported to archives.txt!")

def save_contacts():
    with open(file_name, "w") as f:
        for name, info in contacts.items():
            f.write(f"{name}, {info['Phone']}, {info['Email']}, {info['Address']}\n")

# Main Menu Loop
while True:
    print("\n[SECURITY LEVEL: RED] Jedi Archives Mainframe")
    print("1. Add New Jedi Record")
    print("2. Edit Existing Jedi Record")
    print("3. Remove a Jedi Record")
    print("4. Search Jedi Records")
    print("5. Display all  Jedi Records")
    print("6. Export  Jedi Records Holocron File")
    print("7. Exit Jedi Archives")
    
    choice = input("Enter your command: ").strip()
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        edit_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        export_contacts()
    elif choice == "7":
        print("[NOTICE] Archives going into lockdown. May the Force be with you.")
        break
    else:
        print("[ERROR] Invalid command. Try again, Commander.")

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