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
        input_string is a string in which we search in
        substring is a string in which we search for within input_string
        start is an integer that specifies the starting index from where we start looking
        end is an integer that specifies the end index of where we are looking
    :return:
        an integer: the index position of the first occurrence of the substring within the input_string within indexes
            start and end, otherwise, -1 if the substring could not be found within the indexes start and end.
    :raises:

    """

    substring_length = len(substring)
    for number in range(start, end-substring_length+1):
        match = True
        for letter in range(substring_length):
            if not input_string[number + letter] == substring[letter]:
                match = False
        if match == True:
            return number
    return -1


find("This is an ex-parrot", "parrot", 0, 20)

def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    index = find(input_string,substring,start,end)
    result = ""
    while not index == -1:
        if not result == "":
            result = result + ","
        result = result + str(index)
        index = find(input_string,substring,index + 1,end)


    return result

