#Program for the Contact Management System

#An empty contact list
contacts = []

def add_contact(contact_list, name, phone):
    contact = {"name": name,
               "phone": phone}
    contact_list.append(contact)
    print(f"Contact {name} added successfully")
    view_contacts(contact_list)

def view_contacts(contact_list):
    if not contact_list:
        print("No contacts in the list")
    else:
        for contact in contact_list:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(contact_list, name):
    for contact in contact_list:
        if contact["name"] == name:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        else:
            print("Contact not found")

def delete_contact(contact_list, name):
    for contact in contact_list:
        if contact["name"] == name:
            contact_list.remove(contact)
            print(f"Contact {name} deleted successfully")
            view_contacts(contact_list)

print("Welcome to the Contact Management System")

#while loop for continuing the system
while True:
    
    print("\n Please select an option below: ")
    print("1. Add a new contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name of the contact: ")
        phone = input("Enter the phone number of the contact: ")
        add_contact(contacts, name, phone)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        name = input("Enter the name of the contact: ")
        search_contact(contacts, name)
    elif choice == "4":
        name = input("Enter the name of the contact: ")
        delete_contact(contacts, name)
    elif choice == "5":
        print("Thank you for using the Contact Management System")
        break
    else:
        print("Invalid input")


