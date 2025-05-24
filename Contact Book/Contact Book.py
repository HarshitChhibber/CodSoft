import os.path

contacts = []
file_name = "Contact Book.txt"

def loading_contact():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    contact = {
                        "Name": parts[0].strip(),
                        "Phone": parts[1].strip(),
                    }
                    contacts.append(contact)
        file.close()


def save_contacts():
    with open(file_name, "w") as file:
        for contact in contacts:
            file.write(f"{contact['Name']:<25},{contact['Phone']}\n")


def add_contacts():
    name = input("Enter the Name: ")

    while True:
        phone = input("Enter the Phone No.: ")
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Enter a valid 10 digit Phone No.!")
    contact = {
        "Name": name,
        "Phone": phone,
    }

    contacts.append(contact)
    save_contacts()
    print("Contact added Successfully!")


def view_contacts():
    if not contacts:
        print("No Contacts Found.")
        return

    print("\nContact List =>")
    print("-" * 30 + "\n")
    print(f"{'Name':<20} {'Phone No.':<15}")
    print("-" * 30 + "\n")

    for contact in contacts:
        print(f"{contact['Name']:<20} {contact['Phone']}")


def search_contact():
    if not contacts:
        print("No Contact available.")
        return None, None

    print("Search By ->")
    print("1. Name")
    print("2. Phone No.")
    search = input("Enter your choice (1 or 2): ")
    search_by = input("Enter the Search Term: ")

    for index, contact in enumerate(contacts):
        if search == "1" and contact["Name"].lower() == search_by.lower():
            print("-" * 30 + "\n")
            print(f"Contact Found: \n{contact['Name']:<20} {contact['Phone']}")
            return contact, index
        elif search == "2" and contact["Phone"] == search_by:
            print("Contact Found:")
            print("-" * 30 + "\n")
            print(f"{contact['Name']:<20} {contact['Phone']}")
            return contact, index

    print("Contact not found.")
    return None, None


def edit_contacts():
    contact, index = search_contact()
    if contact is None:
        return

    new_name = input(f"Enter new Name (current: {contact['Name']}): ") or contact['Name']
    new_phone = input(f"Enter new Phone No. (current: {contact['Phone']}): ") or contact['Phone']

    updated_contact = {
        "Name": new_name,
        "Phone": new_phone
    }

    contacts[index] = updated_contact
    save_contacts()
    print("Contact Updated Successfully!")


def delete_contact():
    contact, index = search_contact()
    if contact is None:
        print("No Contact Found.")
        return

    del contacts[index]
    save_contacts()
    print("Contact Deleted Successfully!")


def main_menu():
    iteration = 0

    while True:
        iteration += 1
        if iteration > 1:
            print("------------------------------")
        print("Select an Operation =>")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        menu = input("Enter your choice: ")
        if menu == "1":
            add_contacts()
        elif menu == "2":
            view_contacts()
        elif menu == "3":
            search_contact()
        elif menu == "4":
            edit_contacts()
        elif menu == "5":
            delete_contact()
        elif menu == "6":
            return
        else:
            print("Please Enter a valid option")


loading_contact()
main_menu()