array = [1,2,3,4,5]

print(array)

#add the array to itself
array = array + array 
print (array)



names = ["Alex","John","Mary","Steve","John", "Steve"]


#this removes all the duplicates including commas

print(type(names))
def removeDuplicates(list):
    uniqs = ''
    for x in list:
        if not(x in uniqs):
            uniqs = uniqs + x
    return uniqs
    
print (removeDuplicates(names))



#converting to a dictionary 
#names = list(dict.fromkeys(names))
#print(names)


names_undup = []
def remove_dup():
    for name in names:
        if name not in names_undup:
            names_undup.append(name)
            #print(names_undup)
remove_dup()
print(names_undup)      

check = [0,1,2,3,4,5,6,7,8,9]
numbers = [0,1,2,3,5,6,7,8,9]
for i in range(0, len(check)):
#for i in range(0, 10):
   # print(i)
    #index=(i)
    #print(index)
    print (check[i])
    print (numbers[i])
    if check[i] == numbers[i]:
        print("ok")
    elif check[i] != numbers[i]:
        print(f"{check[i]} is missing")
        break

        
            

    #print(numbers[i])
    
test = "cvfsrstau"
num = len(test)
print (len(test)

string = "geeks" 
print(len(string))