import re


print("\n" + "Magical calculator" + "\n")
print("Version: 1.3.0 \nCreated by Ivaylo Vasilev")
print("=========================")
print("Type 'new' to start new calculation or type 'quit' to exit the program\n")

previous = 0
run = True


def performmath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'new':
        equation = input("Enter new equation:")
        previous = 0

    if equation == 'quit':
        print("\nGoodbye! Thank you for using Magical calculator.")
        run = False
    else:
        equation = re.sub('[A-Za-z:" ]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performmath()
