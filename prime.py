#this will calculate if a number is prime or not
number = int(input("please enter a number: "))

#need to use modulos here somewhere

#mod = 0

#need to check to see if we can divide by any number other than itself and 1
#inputing the number to calculate the range which should take the number itself out of the calc, set the intial range to 2 to avoid the number 1 
for i in range(2, (int(number/2)+1)):
    mod = number % i
    if mod == 0:
        print (number, "is not a prime number")
        # at first number that can divide equally break the loop
        break

else:
     print (number, "is a prime number")        

        

   
   
