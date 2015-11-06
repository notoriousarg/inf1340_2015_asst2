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
    This function looks to see if the substring is present within the input_string, such that the entire substring
    lies between the start and the end indexes of the input_string. This function returns the index of the first
    character of the first occurrence of the substring in the input_string, or -1 otherwise. If the substring is
    an empty string, -1 will be returned.
    The input is assumed to be the correct data types.

    :param input_string: a string in which we search in
    :param substring: a string in which we search for within input_string
    :param start: an integer that specifies the starting index from where we start looking
    :param end: an integer that specifies the end index of where we are looking
    :return: an integer: the index position of the first occurrence of the substring within the input_string within
    indexes start and end, otherwise, -1 if the substring could not be found within the indexes start and end.
    :raises: N/A

    """

    substring_length = len(substring)
    return_value = -1
    if substring_length != 0:
        for input_string_index in range(start, end - substring_length + 1):
            match = True    # Assume string starting at this index matches, then compare.
                            # If letter does not match, word does not match
            for substring_index in range(substring_length):
                if input_string[input_string_index + substring_index] != substring[substring_index]:
                    match = False               # Letter does not match, hence, word does not match
            if match and return_value == -1:    # If no letter mismatch, and return_value is not set (first occurrence),
                                                # then store this index as the return_value
                return_value = input_string_index
    return return_value

def multi_find(input_string, substring, start, end):
    """
    This function looks to see if the substring is present within the input_string, such that the entire substring
    lies between the start and the end indexes of the input_string. This function uses the find() function.
    This function returns a string that contains the integer indices of the occurrences, delimited by commas. If the
    substring is empty, or if the substring is not found within the input_string, an empty string will be returned.
    The input is assumed to be the correct data types.

    :param input_string: a string in which we search in
    :param substring: a string in which we search for within input_string
    :param start: an integer that specifies the starting index from where we start looking
    :param end: an integer that specifies the end index of where we are looking
    :return: a string containing comma-separated integers denoting the indexes of the occurrences that the substring
                was found within the input_string. If no occurrences are found or the substring is empty, an empty
                string is returned.
    :raises: N/A
    """
    index = find(input_string,substring,start,end)
    result = ""
    while not index == -1:
        if not result == "":        # For the first occurrence, no comma is needed before the index
            result = result + ","
        result = result + str(index)
        index = find(input_string,substring,index + 1,end)
    return result

