'my calculator'
print("\n\n\n\n\t\t\t\t\t\t\t\t\t******** WELCOME  TO  MY  CALCULATOR ********\n\n")

print("do you want to calculate?......\n enter y or n\n")
ch = input()
while( ch=='y' or ch=='Y'):
    print("enter your first number: ")
    num1 = int(input())
    print("enter your second number: ")
    num2 = int(input())
    print("enter the operation you wish to have: +,-,*,/,**,//")
    op=input()

    if op=='+':
        print ("Result is : ",num1+num2)


    elif(op=='-'):
        print ("Result is : ",num1 - num2)

    elif (op == '*'):
        print ("Result is : ",num1 * num2)

    elif (op=='/'):
        print ("Result is : ",num1 / num2)

    elif (op == '**'):
        print ("Result is : ",num1 ** num2)

    elif (op == '//'):
        print ("Result is : ",num1 // num2)
    else:
        print("you entered a wrong choice...please try again!!!")

    print("do you want to calculate again?......\n enter y or n")
    ch = input()