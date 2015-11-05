#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

VOWELS = ["a","e","i","o","u"]

def pig_latinify(word):
    """
    Determine if word starts with a vowel or consonant.
    If it starts with a vowel, we append "yay" to the end of the word and return the word.
    Otherwise (it starts with a consonant), we remove all the consonants from the beginning
    of the word up until the first vowel (not removing the vowel). Then we add all these removed
    consonants to the end, and append "ay" after the consonants. Any input that is not all alphabetic
    characters or those without vowels will raise a value error.

    :param : word should be a string
    :return: the pig-latinified word as a string
    :raises: ValueError

    """

    if not isinstance(word,basestring): # Assert that word is in fact a string data type
        raise ValueError
    if not word.isalpha():              # Assert that word only contains characters (no spaces/blank, no numbers, etc.)
        raise ValueError
    if word[0] in VOWELS:               # Check if the first letter is a vowel
        result = word + "yay"
    else:
        index_of_first_vowel = 0        # Find the index of first vowel to do string splicing later
        for index in range(len(word)):
            if word[index] in VOWELS and index_of_first_vowel == 0:
                index_of_first_vowel = index
        if index_of_first_vowel == 0:   # No vowel is present in the word
            raise ValueError
        result = word[index_of_first_vowel:] + word[:index_of_first_vowel] + "ay"

    return result