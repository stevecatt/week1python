word=input("Please enter a word: ")

test_word = word.lower()

word_rev = ""
for i in range(1,len(test_word)+1):
    word_rev += test_word[-i]
    

print (word_rev)

if test_word == word_rev:
    print(f"Weve got a winner {word} is palindromic")

else:
    print(f"Sorry {word} is not a palindrome")