class Node:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Add record (Insert at end)
    def add_record(self, name, phone):
        new_node = Node(name, phone)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Record added successfully!")

    # Linear Search
    def search_record(self, name):
        temp = self.head
        while temp:
            if temp.name == name:
                print("Phone number:", temp.phone)
                return
            temp = temp.next
        print("Record not found!")

    # Modify record
    def modify_record(self, name, new_phone):
        temp = self.head
        while temp:
            if temp.name == name:
                temp.phone = new_phone
                print("Record modified successfully!")
                return
            temp = temp.next
        print("Record not found!")

    # Delete record
    def delete_record(self, name):
        temp = self.head
        prev = None

        while temp:
            if temp.name == name:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print("Record deleted successfully!")
                return
            prev = temp
            temp = temp.next

        print("Record not found!")

    # List records
    def list_records(self):
        print("\nTelephone Directory:")
        temp = self.head
        while temp:
            print(f"{temp.name}: {temp.phone}")
            temp = temp.next

    # Convert SSL to list (helper for sorting)
    def to_list(self):
        data = []
        temp = self.head
        while temp:
            data.append([temp.name, temp.phone])
            temp = temp.next
        return data

    # Rebuild SSL from list (after sorting)
    def from_list(self, data):
        self.head = None
        for name, phone in data:
            self.add_record(name, phone)

    # Bubble Sort
    def bubble_sort(self):
        data = self.to_list()
        n = len(data)

        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j][0] > data[j + 1][0]:
                    data[j], data[j + 1] = data[j + 1], data[j]

        self.from_list(data)
        print("Records sorted using Bubble Sort!")

    # Quick Sort
    def quick_sort(self):
        data = self.to_list()

        def qs(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2][0]
            left = [x for x in arr if x[0] < pivot]
            middle = [x for x in arr if x[0] == pivot]
            right = [x for x in arr if x[0] > pivot]
            return qs(left) + middle + qs(right)

        sorted_data = qs(data)
        self.from_list(sorted_data)
        print("Records sorted using Quick Sort!")


# -------------------------
# Menu-driven program
# -------------------------

directory = LinkedList()

while True:
    print("\nTelephone Directory System")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Modify Record")
    print("4. List Records")
    print("5. Delete Record")
    print("6. Bubble Sort Records")
    print("7. Quick Sort Records")
    print("8. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        directory.add_record(name, phone)

    elif choice == "2":
        name = input("Enter name to search: ")
        directory.search_record(name)

    elif choice == "3":
        name = input("Enter name to modify: ")
        phone = input("Enter new phone number: ")
        directory.modify_record(name, phone)

    elif choice == "4":
        directory.list_records()

    elif choice == "5":
        name = input("Enter name to delete: ")
        directory.delete_record(name)

    elif choice == "6":
        directory.bubble_sort()

    elif choice == "7":
        directory.quick_sort()

    elif choice == "8":
        break

    else:
        print("Invalid choice. Please try again!")
