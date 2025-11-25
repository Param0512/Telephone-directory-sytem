# Telephone Directory System

telephone_directory = {}

def add_record():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    telephone_directory[name] = phone_number
    print("Record added successfully!")

def search_record():
    name = input("Enter name to search: ")
    if name in telephone_directory:
        print("Phone number: ", telephone_directory[name])
    else:
        print("Record not found!")

def modify_record():
    name = input("Enter name to modify: ")
    if name in telephone_directory:
        new_phone_number = input("Enter new phone number: ")
        telephone_directory[name] = new_phone_number
        print("Record modified successfully!")
    else:
        print("Record not found!")

def list_records():
    print("Telephone Directory:")
    for name, phone_number in telephone_directory.items():
        print(f"{name}: {phone_number}")

def delete_record():
    name = input("Enter name to delete: ")
    if name in telephone_directory:
        del telephone_directory[name]
        print("Record deleted successfully!")
    else:
        print("Record not found!")

while True:
    print("\nTelephone Directory System")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Modify Record")
    print("4. List Records")
    print("5. Delete Record")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        search_record()
    elif choice == "3":
        modify_record()
    elif choice == "4":
        list_records()
    elif choice == "5":
        delete_record()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again!")