
print 'Try to guess the word I m thinking of.'
print 'If the word you guess comes after my word'
print 'in the dictionary, I will say: too far'
print 'If the word you guess comes before my word,'
print 'I will say: go farther.'

import randomword
guess=1
count=1
theanswer=randomword.randomword()
while guess != theanswer and (count<41):
    count=count+1
    guess=raw_input('Enter your guess: ')
    if guess < theanswer:
        print 'go further'
    if guess > theanswer:
        print 'too far'
if guess == theanswer:
    print 'Good job you found it, and you did so in',count, 'guesses'
if count == 21:
    print 'You had your 20 guesses, you lost'

