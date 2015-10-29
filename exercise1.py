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
    Determine if word starts with a vowel or constonant.
    If it starts with a vowel, we append "yay" to the end of the word and return the word.
    Otherwise (it starts with a constonant), we remove all the constonants from the beginning
      of the word up until the first vowel (not removing the vowel). Then we add all these removed
      constonants to the end, and append "ay" after the constonants.

    :param : word should be a string
    :return: the pig_latinified word as a string
    :raises: ValueError

    """

    if not isinstance(word,basestring):
        raise ValueError
    if not word.isalpha():
        raise ValueError
    if word[0] in VOWELS:
        result = word + "yay"
    else:
        index_of_first_vowel = 0
        index_counter = 0
        for letter in word:
            if letter in VOWELS and index_of_first_vowel == 0:
                index_of_first_vowel = index_counter
            index_counter = index_counter + 1
        result = word[index_of_first_vowel:] + word[:index_of_first_vowel] + "ay"

    return result