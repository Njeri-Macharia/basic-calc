import operatorfunction
while True:
    first_number=float(input('Enter first number: '))
    second_number=float(input('Enter second number: '))
    print('type quit to exit the calculator')
    operand_used=input('Enter the operator to use(+,-,/,*,**,quit):')


    if operand_used=='+':
        print (operatorfunction.addition(first_number,second_number))

    elif operand_used=='-':
        print(operatorfunction.subtraction(first_number,second_number))

    elif operand_used=='/':
        print(operatorfunction.division(first_number,second_number))

    elif operand_used=='*':
        print(operatorfunction.multiplication(first_number,second_number))

    elif operand_used=='**':
        print(operatorfunction.square(first_number,second_number))
    elif operand_used.lower()=='quit':
        break

    else:
        print('use the correct operator')