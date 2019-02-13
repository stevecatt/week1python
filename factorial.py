#this will calculate the factoriol of the input number


number = int(input("please enter a number: "))
factor = 1
for i in range(1, number+1):
    #print(n)
    factor = factor * i

print(f"The factoriol of {number} is {factor}")
