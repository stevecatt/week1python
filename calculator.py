#calculator app
#need three inputs from user in one statement
num1 = input("Please enter a number: ")
oper = input("please enter operand +,-,/ or *: ")
num2 = input ("please enter second number: ")

#set up functions
def add():
    print (int(num1) + int(num2))

def sub():
    print(int(num1) - int(num2))

def divide():
    print(int(num1) / int(num2))


def mult():
    print(int(num1) * int(num2))

# check the operand to see which function to use 
if oper == "+":
    add()
    
if oper == "*":
    mult()

if oper == "-":
    sub()

if oper == "/":
    divide()
 