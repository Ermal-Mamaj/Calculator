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


    if choice == "a":
        print("Addition")
        a = input("First number: ")
        b = input("Second number: ")
        Addition(int(a),int(b))
    elif choice == "b":
        print("Subtraction")
        a = input("First number: ")
        b = input("Second number: ")
        Subtraction(int(a),int(b))
    if choice == "c":
        print("Multiplication")
        a = input("First number: ")
        b = input("Second number: ")
        Multiplication(int(a),int(b))
    if choice == "d":
        print("Devision")
        a = input("First number: ")
        b = input("Second number: ")
        Devision(int(a),int(b))
    elif choice == "e":
        print("\nProgram ended")
        quit()
