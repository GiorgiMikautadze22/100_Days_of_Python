import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multipy(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multipy,
    '/': divide
}

initial_number = int(input("Input First Number: "))
def calculator(n1):
    method = input("What method do you want to perform? +, -, * or / : ")
    n2 = int(input("Input Next Number: "))

    result = operations[method](n1, n2)
    print(f"{n1} {method} {n2} = {result}")
    continue_calc = input('Do you want to continue calculation on this number? ').lower()
    if continue_calc == 'yes':
        os.system("cls")
        calculator(result)
    else:
        return "Good By"

calculator(initial_number)