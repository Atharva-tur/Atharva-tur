list_item = []

while True:
    print("\n....List....\n")
    print("1. Add item")
    print("2. Visit list")
    print("3. Remove element")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add to list: ")
        list_item.append(item)
        print("Item is added...")

    elif choice == 2:
        print("Your list:", list_item)

    elif choice == 3:
        if not list_item:
            print("List is empty, nothing to remove.")
        else:
            print("Current list:", list_item)
            remove = input("Enter item you want to remove: ")
            if remove in list_item:
                list_item.remove(remove)
                print("Item is removed.")
            else:
                print("Item not found in the list.")

    elif choice == 4:
        print("Goodbye....")
        break

    else:
        print("Enter valid number...")