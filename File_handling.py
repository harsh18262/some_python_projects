#basic file handling program to add vie and remove contents from a file

print("which function do you want to perform?\n1)add\n2)view\n3)remove")
option = int(input())
if option == 1:
    name = input("Enter name")
    age = input("enter age")
    newfile = open("abc.txt", "a")
    string = (name + " " + age + "\n")
    newfile.write(string)
    newfile.close()
    print("Name and age stored in the file")
elif option == 2:
    newfile = open("abc.txt", "r+")

    strings = [line for line in newfile.readlines()]
    num = len(strings)

    count = 0
    while count < num:
        string = strings[count:count + 1]
        name, age = string[0].split(" ")
        print((str(count + 1)) + "." + name)
        count = count + 1

    newfile.close()
    print("Whose age do you want to know\n")
    choice = input("enter your choice")

    name, age = strings[int(choice) - 1].split(" ")

    print(age)

elif option == 3:
    print("Who do you want to delete\n")

    newfile = open("abc.txt", "r+")

    strings = [line for line in newfile.readlines()]

    num = len(strings)

    count = 0
    while count < num:
        string = strings[count:count + 1]
        name, age = string[0].split(" ")
        print((str(count + 1)) + "." + name)
        count = count + 1
        newfile.close()

    choice = int(input("select your option\n"))

    src_file = "abc.txt"

    f = open(src_file, "r")

    contents = f.readlines()

    f.close()

    contents.pop(choice - 1)

    f = open(src_file, "w")
    contents = "".join(contents)

    f.write(contents)
    f.close()
