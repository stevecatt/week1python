#string = "geeks" 
#print(len(string))
names = ["Alex","John","Mary","Stevehen"]
print (max(names))

for name in names: 
    #print(len(name), name)
    length = {'le': len(name), 'name': name }
    #print(length)
    #print (max(length("length")))
    #print (max(length["length"]))
    #print(length["length"])
    print (f" - {length['le']} - {length['name']}")
    #print (length.items())
    for key,value in length.items():
         print(key,value)


    #trying to figure out how to get the max lenght out of this dictionary 

    #max = 0
    #for l in length["le"]:
     #   if l > max:
      #      max= l
       #     print (length["le"])

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