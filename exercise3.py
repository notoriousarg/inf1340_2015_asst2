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
    """
    This function compares two list of lists (table1 and table2) and outputs True if the tables have the same
        schema, or False otherwise. This is done first by comparing the lengths of the schema list. If different,
        then the schemas do not match. Otherwise if the lengths of the schemas are the same, then we need to check
        each item of the schema such that if one index from table1[0] fails to match its corresponding index in
        table2[0], respective to their positions, then we can return False. If no such mis-match is found, True
        is returned.
    :param table1: List of lists with at least one list inside: the schema is the first list.
    :param table2: List of lists with at least one list inside: the schema is the first list.
    :return: True if table schema matches, or more specifically, if table1[0] and table2[0] are equivalent
    """
    match = True    #Assume the tables match unless some mismatch occurs.
    if len(table1[0]) == len(table2[0]):
        for number in range(len(table1[0])):
            if not table1[0][number] == table2[0][number]:
                match = False
    else:
        match = False
    return match



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
        raise MismatchedAttributesException
    union_list = []
    for item in table1:
        union_list += item     #Deep copy of table1, including the schema

    for item in table2:
        if item not in union_list
            union_list += item

    return union_list


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

