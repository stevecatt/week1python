word = input("please input a word: ")
#make sure word is lower case for test
test_word = word.lower()
#Reverse the input word (easy way)
# start stop step 
rev_word = test_word [::-1]





#

#Test print



if rev_word == test_word:
    print(f"We got a wimmer {word} is a palindrome")

else:
    print (f"{word} is not a palindrome")