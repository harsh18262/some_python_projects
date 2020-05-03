todolist = []

while True:
    print("Welcome to my To-Do List\n")
    print("1)Add an item\n2)Mark an item as done\n3)View the list\n4)quit")
    choice = int(input("enter your choice\n"))

    if choice == 1:
        data = input("what do you want to add?")
        todolist.append(data)

    elif choice == 2:
        data = input("what item do you want to mark as done\n")
        if data in todolist:
            todolist.remove(data)
        else:
            print("item is not present in the list")

    elif choice == 3:
        print("To-Do List:-")
        i = 1
        for item in todolist:
            print(str(i)+")", item)
            i += 1

    elif choice == 4:
        exit("Bye")

    else:
        print("enter a valid option")
