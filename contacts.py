
import json

import os

def main():
    print("contact list")
    print("load contacts")
    print("save contacts")
    print("1. add contacts: ")
    print("2. view contact: ")
    print("3. update contact: ")
    print("4. delete contact: ")
    
contacts_file= 'contacts_data.json'


def load_contacts():
    if not os.path.exists(contacts_file):
        return {}
    try:
        with open(contacts_file, 'r') as file:
            return json.load(file)
    except Exception as e:
  
        print(f"Enter loading contacts data: {e}")
        return {}
    

def save_contact(contacts):
    try:
        with open(contacts_file, 'w') as file:
            json.dump(contacts,file)
    except Exception as e:
        print(f"Error saving contacts data: {e}")
        

def add_contact(contacts,name,phone,email):
    if name in contacts:
        print("Contact already exists. Use udate option to modify.")
    else:
        contacts[name] = {'phone': phone,'email': email}

        save_contact(contacts)

        print(f"Contact '{name}' added successfully!")

        
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")


def update_contact(contacts, name, phone=None, email=None):
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    save_contact(contacts)

    print(f"contact ' {name} updated successfully!")


def delete_contacts(contacts,name):
    if name not in contacts:
        print(f"contact ' {name}' not foundd.")
        return
    del contacts[name]
    save_contact(contacts)

    print(f"Contacts '{name}' deleted successfully!")



      
def main():
    contacts = load_contacts()
    while True:
        choice=input("enter your choice: ")
        if choice == "1":
            name = input("Enter the contact name: ")
            phone = input("Enter the contact phone number: ")
            email = input("Enter the contact email: ")
            add_contact(contacts, name, phone, email)
        elif choice ==  "2":
            view_contacts(contacts)
        elif choice == "3":
            neme = input("Enter the contact name to update: ")
            phone = input("Enter the new phone number (leave blank to keep current)")
            email = input("Enter the new email (leave blank to keep current): ")
            add_contact(contacts, name, phone if phone else None, email if email else None)
        elif choice == "4":
            name = input("Enter the contact name to delete: ")
            delete_contacts(contacts, name)
        
        elif choice == "5":
            print("Exiting the system. goodbye!")
            break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

if __name__=="__main__":
    main()
            


    




   