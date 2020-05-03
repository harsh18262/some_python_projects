import re
print("loop calculator\n type quit to exit")

result = 0

quitp = True
while quitp:
    result
    equation = ""
    if result == 0:
        equation = input("enter a equation")
    else:
        equation = input(str(result))
    if equation == 'quit':
        exit("\nBye See You Soon")
    else:
        equation = re.sub('[a-zA-Z,.:()" "],', '', equation)

        if result == 0:
            result = eval(equation)
        else:
            result = eval(str(result) + equation)
