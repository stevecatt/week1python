number = input("Please enter a whole number: ")


#test if number is divisible by both 3 % 5
if int(number) % 3 == 0 and int(number) % 5 == 0:
    print("FizzBuzz")

# if not then test if divisible by 3
elif int(number) % 3 == 0:
    print("Fizz")

# in not test if divisible by 5
elif  int(number) % 5 == 0:
    print ("Buzz")

