# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 00:46:57 2021

@author: Asus
"""

def match_with_gaps(my_word, other_word):
    a = my_word.replace(" ", "")
    for i in range(0, len(a.strip())):
        if len(a) != len(other_word):
            return False
        if a[i] == other_word[i] :
            continue
        if a[i] == "_":
            continue
        else :
            return False
    return True

my_word = input("enter:")
other_word = input("enter:")
print(match_with_gaps(my_word, other_word))
