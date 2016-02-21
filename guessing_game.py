#A guessing game

import randomword

print "Try to guess the word I'm thinking of."
print "If the word you guess comes after my word"
print "in the dictionary, I will say 'too far'."
print "If the word you guess comes before my word,"
print "I will say, 'go farther'."
count = 1
secret_word=randomword.randomword()
guess = raw_input("Enter your guess:\n")
while(guess!=secret_word):
    if guess < secret_word:
        print 'go farther'
    elif guess > secret_word:
        print 'too far'
    guess = raw_input("Enter your guess:\n")
    count += 1
    if count > 40:
        break

if count<=40:
    print 'You got it! It took you ',count,' guesses.'
else:
    print 'This is getting ridiculous.  The secret word is ',secret_word
