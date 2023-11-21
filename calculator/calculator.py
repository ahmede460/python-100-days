#Calculator
end = False
#Add
def add(num1,num2):
    return num1 + num2
#Sub
def sub(num1,num2):
    return num1 - num2
#Multiply
def multiply(num1,num2):
    return num1 * num2
#Division
def divide(num1,num2):
    return num1 / num2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}

while 1 != 2:
        
    number1 = int(input("Welcome to the python calculator, enter your first number : "))
    number2 = int(input("Welcome to the python calculator, enter your second number : "))

    for symbol in operations:
        print(symbol)

    operation = input("Pick an operation from the line above : ")

    calc = operations[operation]
    answer = calc(number1,number2)

    print(f"{number1} {operation} {number2} = {answer} \n \n")

    while end == False:


        for symbol in operations:
            print(symbol)
        operation = input("Pick another operation : ")
        number3 = int(input("enter your another number : "))

        calc = operations[operation]
        secondanswer = calc(answer,number3)

        print(f"{answer} {operation} {number3} = {secondanswer} \n \n")

        answer = secondanswer

        choice = input("Do you want to do another operation ? Y/N ")
        if choice == "Y":
            end = False
        else:
            end = True
