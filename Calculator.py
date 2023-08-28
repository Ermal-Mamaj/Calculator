def Addition(a,b):
    result = a + b
    print(f'{a} + {b} = {result}\n')
def Subtraction(a,b):
    result = a - b
    print(f'{a} - {b} = {result}\n')
def Multiplication(a,b):
    result = a * b
    print(f'{a} * {b} = {result}\n')
def Devision(a,b):
    result = a / b
    print(f'{a} / {b} = {result}\n')

while True:

    print("A.Addition")
    print("B.Subtraction")
    print("C.Multiplication")
    print("D.Devision")
    print("E.Exit")
    choice= input("Input your choise: ").lower()


    if choice == "a" or choice.lower == "addition":
        print("Addition")
        a = input("First number: ")
        b = input("Second number: ")
        Addition(int(a),int(b))
    elif choice == "b" or choice.lower == "subtraction":
        print("Subtraction")
        a = input("First number: ")
        b = input("Second number: ")
        Subtraction(int(a),int(b))
    if choice == "c" or choice.lower == "multiplication":
        print("Multiplication")
        a = input("First number: ")
        b = input("Second number: ")
        Multiplication(int(a),int(b))
    if choice == "d" or choice.lower == "devision":
        print("Devision")
        a = input("First number: ")
        b = input("Second number: ")
        Devision(int(a),int(b))
    elif choice == "e" or choice.lower == "exit":
        print("\nProgram ended")
        quit()
    else:
        print("Couldn't find your choise")
        print("Please try again")
