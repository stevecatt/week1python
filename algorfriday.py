array = [1,2,3,4,5]
names = ["Alex","John","Mary","Steve","John", "Steve"]


print (f"The largest string in the array is : {max(names)} " )
print (f"The smallest string in array is {min(names)} ")


array = array + array 
print (array)


#remove duplicate names 

names_undup = []
def remove_dup():
    for name in names:
        if name not in names_undup:
            names_undup.append(name)
            #print(names_undup)
remove_dup()
print(f"The list of unduplicated names is {names_undup} ")   

# check for missing value

check = [0,1,2,3,4,5,6,7,8,9]
numbers = [0,1,2,3,5,6,7,8,9]
for i in range(0, len(check)):
    #print (check[i])
    #print (numbers[i])
    if check[i] == numbers[i]:
        print(f"Ok that number {check[i]} is there")
    elif check[i] != numbers[i]:
        print(f"Number {check[i]} is missing")
        break





a=[1,2,3,4,6,7,99,88,999]
max= 0
for i in a:
    if i > max:
         max=i
print(max) 


a=[1,2,3,4,6,7,99,88,999]
min= 10000
for i in a:
    if i <= min:
         min=i
print(min)



for name in names:
    #print(len(name), name)
    length = {'le': len(name), 'name': name }
    #print(length)
    #print (max(length("length")))
    #print (max(length["length"]))
    #print(length["length"])
    print (f" - {length['le']} - {length['name']}")

    #trying to figure out how to get the max lenght out of this dictionary 

    #max = 0
    #for l in length["le"]:
     #   if l > max:
      #      max= l
       #     print (length["le"])
