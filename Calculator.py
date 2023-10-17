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

calculate = True

while calculate:
    print("\nSelect operation!\n")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Devision")
    print("5.Exit")
    choice= input("Input your choise: ").lower()


    if choice == "1" or choice.startswith("a"):
        a = input("First number: ")
        b = input("Second number: ")
        Addition(int(a),int(b))
    elif choice == "2" or choice.startswith("s"):
        print("Subtraction")
        a = input("First number: ")
        b = input("Second number: ")
        Subtraction(int(a),int(b))
    elif choice == "3" or choice.startswith("m"):
        print("Multiplication")
        a = input("First number: ")
        b = input("Second number: ")
        Multiplication(int(a),int(b))
    elif choice == "4" or choice.startswith("d"):
        print("Devision")
        a = input("First number: ")
        b = input("Second number: ")
        Devision(int(a),int(b))
    elif choice == "5" or choice.startswith("e"):
        print("\nProgram ended")
        quit()
    else:
        print("Couldn't find your choise")
        print("Please try again")
    calculate = input("Do u want to calculate agin: ").lower()
    print("\n\n")
    if calculate.startswith("y"):
        calculate = True
    else:
        calculate = False
