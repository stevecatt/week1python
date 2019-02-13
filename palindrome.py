word = input("please input a word: ")
#make sure word is lower case for test
test_word = word.lower()

#create a variable called lenght for string length 
length = len(test_word)
#create the reverse word to be compared 
word_rev = ""


while length>0:
   word_rev += test_word[length-1]
   length = length-1

#printing the revesre word out to see what it looks like

print (word_rev)

if test_word == word_rev:
    print(f"Weve got a winner {word} is palindromic")

else:
    print(f"Sorry {word} is not a palindrom")