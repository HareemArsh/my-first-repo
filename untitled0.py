# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 21:46:08 2021

@author: Asus
"""

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string 
    s = string.ascii_lowercase
    print (s)
    a = list(s)

    for i in letters_guessed:
        if i in a:
            a.pop(i)
    print("".join(a))
        
    
letters_guessed = (input("enter letter guessed:", ))
print(get_available_letters(letters_guessed))


#c = alphabets.translate({ord(i): None})

if guess not in letters_guessed and guess in secret_word:
                letters_guessed += guess
            
                print('Good guess:' + get_guessed_word(secret_word, letters_guessed))
            
                if guess in 'aeiou':
                    num_guesses -= 2
                else:
                    num_guesses -= 1
                print('Ops! that letter is not in my secret word:' + get_guessed_word(secret_word, letters_guessed)
            else:
                if warnings  > 0:
                   warnings -= 1
                   print("Oops! You've already guessed that letter and you have remaining " + warnings "warnings left :" + get_guessed_word(secretWord, lettersGuessed))
                else:
                    num_guesses -=1 
                    print(print("Oops! You've already guessed that letter and you have remaining " + num_guesses "guesses left :" + get_guessed_word(secretWord, lettersGuessed))) 
 