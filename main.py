import re

print("Script Calculator\n")

run = True
previous = None


def perform_Math():
    global run
    global previous
    equation = ""

    if previous is None:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    if equation == "End" or equation == "end":
        print("adios!")
        run = False
    else:
        equation = re.sub('[a-zA-z,.;()" "]', '', equation)

        if previous is None:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_Math()