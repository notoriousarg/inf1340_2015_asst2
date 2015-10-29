#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

def test_non_alphabetic():
    """
    Test non-alphabetic words
    """
    non_alphabetic_words = ["sd12d", "a25d", ",.{}-", "2153", 2523, "get.it.done", True, 24.25, "two words"]
    for item in non_alphabetic_words:
        try:
            assert pig_latinify(item)
            assert False
        except ValueError:
            assert True