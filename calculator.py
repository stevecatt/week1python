#calculator app
#need three inputs from user in one statement
# better with num1 = int(input("enter number"))
# decided to create functions that could be called later but for this exercise it was too wordy 


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

# check the operand to see which function to use elifs would use less resources
# could have done all this in one go
if oper == "+":
    add()
    
if oper == "*":
    mult()

if oper == "-":
    sub()

if oper == "/":
    divide()
 