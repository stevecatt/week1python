names = ["john","mary","ann","jeff","sue","bubba"]
for i in range(0,len(names)):
    print(names[i])

#another way

names.append("burt")
for name in names:
    print(name)

del names[2]

for name in names:
    print(name)
