#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def table_match(table1, table2):
    if len(table1[0]) == len(table2[0]):
        match = True
        for number in range(len(table1[0])):
            if not table1[0][number] == table2[0][number]:
                match = False
        if match == True:
            return True
    return False



def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.



    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    if not table_match(table1, table2):
        raise ERROR



    return []


def intersection(table1, table2):
    """
    Describe your function

    """
    return []


def difference(table1, table2):
    """
    Describe your function

    """
    return []


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

