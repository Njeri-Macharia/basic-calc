#functions for calculator operations
def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    if num1==0 or num2==0:
        print("ZERO CANNOT DIVIDE A NUMBER")
    else:
        return num1/num2 

def square(num1,num2):
    return num1**num2    