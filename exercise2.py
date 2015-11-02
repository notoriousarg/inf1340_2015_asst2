#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """

    input_string_length = len(input_string)
    substring_length = len(substring)


    for number in range(input_string_length-substring_length):
        match = True
        for letter in range(substring_length):
            if not input_string[number + letter] == substring[letter]:
                match = False
        if match == True:
            return number
    return -1




def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result

