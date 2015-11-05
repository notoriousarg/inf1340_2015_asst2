#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14
    assert find("This is an ex-parrot", "parrot", 14, 20) == 14
    assert find("Who lives in a pineapple under the sea", "sea", 0, 38) == 35

def test_find_not_present():
    """
    Test find function when substring is not present in input_string, or outside index range.
    """
    assert find("This is an ex-parrot", "parrot", 0, 19) == -1
    assert find("This is an ex-parrot", "parrot", 15, 20) == -1
    assert find("Who lives in a pineapple under the sea", "sea", 0, 30) == -1
    assert find("", "parrot", 0, 0) == -1

def test_find_substring_larger_than_input_string():
    """
    Test find function with a substring length larger than the input string length.
    """
    assert find("parrot", "This is an ex-parrot", 0, 6) == -1
    assert find("", "parrot", 0, 0) == -1

def test_find_substring_larger_than_input_string():
    """
    Test find function with an empty substring.
    """
    assert find("parrot", "", 0, 0) == -1
    assert find("", "", 0, 0) == -1

def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 15) == "0,4,8,12"
    assert multi_find("Catdogcatdog", "cat", 0, 12) == "6"
    assert multi_find("Catdogcatdog", "Cat", 0, 12) == "0"
    assert multi_find("Catdogcatdog", "dog", 0, 12) == "3,9"
    assert multi_find("aaaaa", "a", 0, 5) == "0,1,2,3,4"
    assert multi_find("aaaaa", "aaaaa", 0, 5) == "0"
    assert multi_find("aaaaa", "aaa", 1, 4) == "1"

def test_multi_find_overlap():
    """
    Test multi_find function.
    """
    assert multi_find("lololololol", "lol", 0, 11) == "0,2,4,6,8"
    assert multi_find("lololololol", "lol", 3, 10) == "4,6"
    assert multi_find("aaaaa", "aa", 0, 5) == "0,1,2,3"
    assert multi_find("aaaaa", "aaa", 0, 5) == "0,1,2"
    assert multi_find("aaaaa", "aaa", 1, 5) == "1,2"

def test_multi_find_basic_not_present():
    """
    Test multi_find function when substring is not present in input_string, or outside index range.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "ni", 0, 15) == ""
    assert multi_find("Who lives in a pineapple under the sea", "spongebob", 0, 38) == ""
    assert multi_find("Who lives in a pineapple under the sea", "sea", 0, 30) == ""
    assert multi_find("", "ni", 0, 0) == ""

def test_multi_find_substring_larger_than_input_string():
    """
    Test multi_find function with a substring length larger than the input string length.
    """
    assert multi_find("parrot", "This is an ex-parrot", 0, 6) == ""
    assert multi_find("", "parrot", 0, 0) == ""

def test_find_substring_larger_than_input_string():
    """
    Test multi_find function with an empty substring.
    """
    assert multi_find("parrot", "", 0, 0) == ""
    assert multi_find("", "", 0, 0) == ""
