word=input("Please enter a word: ")
# can do this in input or within function dont need to creat test_word
test_word = word.lower()

word_rev = ""
for i in range(1,len(test_word)+1):
    word_rev += test_word[-i]
    
# just did this to check 
#print (word_rev)

if test_word == word_rev:
    print(f"Weve got a winner {word} is palindromic")

else:
    print(f"Sorry {word} is not a palindrome")