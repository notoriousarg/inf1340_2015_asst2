#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

EMPLOYEES = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38],
            [0001, "Grey", 45],
            [0002, "Locke", 40],
            [0003, "Hughes", 59]]

OWNER = [["Number","Surname","Age"],
         [0000,"Jeff", 55]]

PETS = [["Species", "Name"],
        ["Cat", "Lola"],
        ["Cat", "Junior"],
        ["Dog", "Tini"]]

#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    if t1 is None or t2 is None:
        return t1 == t2
    else:
        return sorted(t1) == sorted(t2)


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """
    # Something of a table in common
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))
    assert is_equal(result, union(MANAGERS, GRADUATES))

    # All of one table in common
    result = [["Number", "Surname", "Age"],
                [9297, "O'Malley", 56],
                [7432, "O'Malley", 39],
                [9824, "Darkes", 38],
                [0001, "Grey", 45],
                [0002, "Locke", 40],
                [0003, "Hughes", 59]]

    assert is_equal(result, union(MANAGERS, EMPLOYEES))
    assert is_equal(result, union(EMPLOYEES, MANAGERS))

    #Exactly the same table
    assert is_equal(PETS, union(PETS, PETS))

    # Nothing intersecting
    result = [["Number", "Surname", "Age"],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38],
              [0000,"Jeff", 55]]
    assert is_equal(result, union(MANAGERS, OWNER))
    assert is_equal(result, union(OWNER, MANAGERS))

def test_union_mismatch_schema():
    try:
        union(PETS, EMPLOYEES)
        assert False
    except:
        assert True
    try:
        union(MANAGERS, PETS)
        assert False
    except:
        assert True

def test_intersection():
    """
    Test intersection operation.
    """
    # Something of a table in common
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))
    assert is_equal(result, intersection(MANAGERS, GRADUATES))

    # All of one table in common
    result = [["Number", "Surname", "Age"],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(EMPLOYEES, MANAGERS))
    assert is_equal(result, intersection(MANAGERS, EMPLOYEES))

    #Exactly the same table
    assert is_equal(PETS, intersection(PETS, PETS))

    # Nothing intersecting
    assert is_equal(None, intersection(OWNER, MANAGERS))
    assert is_equal(None, intersection(MANAGERS, OWNER))

def test_intersection_mismatch_schema():
    try:
        intersection(PETS, EMPLOYEES)
        assert False
    except:
        assert True
    try:
        intersection(OWNER, PETS)
        assert False
    except:
        assert True

def test_difference():
    """
    Test difference operation.
    """
    # Something of a table in common
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]
    assert is_equal(result, difference(GRADUATES, MANAGERS))

    result = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56]]
    assert is_equal(result, difference(MANAGERS, GRADUATES))

    # All of one table in common
    result = [["Number", "Surname", "Age"],
              [0001, "Grey", 45],
              [0002, "Locke", 40],
              [0003, "Hughes", 59]]
    assert is_equal(result, difference(EMPLOYEES, MANAGERS))

    assert is_equal(None, difference(MANAGERS, EMPLOYEES))

    #Exactly the same table
    assert is_equal(None, difference(PETS, PETS))

    # Nothing intersecting
    assert is_equal(OWNER, difference(OWNER, MANAGERS))
    assert is_equal(MANAGERS, difference(MANAGERS, OWNER))

def test_difference_mismatch_schema():
    try:
        difference(PETS, EMPLOYEES)
        assert False
    except:
        assert True
    try:
        difference(GRADUATES, PETS)
        assert False
    except:
        assert True