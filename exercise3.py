#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"



def union(table1, table2):
    """
    This function tries to perform the union set operation on tables, table1 and table2. If the tables are not
    union-compatible, a MismatchedAttributesException is raised.
    Everything in table1 and table2 is copied to a combined list and the helper function remove_duplicates() is
    called to removes duplicate values is: only unique values remain. The combined list is returned as the output.

    :param table1: List of lists with at least one list inside: the schema is the first list.
    :param table2: List of lists with at least one list inside: the schema is the first list.
    :return: A list of lists denoting a table with the union result: the schema (list) remains as the first item.
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    if not table_match(table1, table2):
        raise MismatchedAttributesException
    union_table = []

    for row in table1:
        union_table.append(row)     #Deep copy of table1, including the schema

    for row in table2:
        union_table.append(row)     #Deep copy of table2, including the schema

    union_table = remove_duplicates(union_table)    # Remove duplicates, including schema
                                                    # Only second + occurrence removed, so schema stays as first item

    return union_table


def intersection(table1, table2):
    """
    This function tries to perform the intersection set operation on tables, table1 and table2. If the tables are not
    intersection-compatible, a MismatchedAttributesException is raised.
    Each row of a table is checked to see if it is present in the other table. If it is present, i.e. it is in both
    tables, then it will be in the table to be returned. This list of common lists is returned as the output.

    :param table1: List of lists with at least one list inside: the schema is the first list.
    :param table2: List of lists with at least one list inside: the schema is the first list.
    :return: A list of lists denoting a table with the intersection result: the schema (list) remains as the first item.
    :raises: MismatchedAttributesException: if tables t1 and t2 don't have the same attributes.
    """
    if not table_match(table1, table2):
        raise MismatchedAttributesException
    intersection_table = []
    for row in table1:
        if row in table2:
            intersection_table.append(row)
    return intersection_table


def difference(table1, table2):
    """
    This function tries to perform the difference set operation on tables, table1 and table2. If the tables are not
    difference-compatible, a MismatchedAttributesException is raised.
    A new list is created with an extra copy of the schema. Then everything in table1 is duplicated into this new
    list, including a second copy of the schema. Table2 is traversed to see if the row is present in the new
    list: if present, that row is removed from the new list. The final list is returned as the output.

    :param table1: List of lists with at least one list inside: the schema is the first list.
    :param table2: List of lists with at least one list inside: the schema is the first list.
    :return: A list of lists denoting a table with the difference result: the schema (list) remains as the first item.
    :raises: MismatchedAttributesException: if tables t1 and t2 don't have the same attributes.
    """
    difference_table = []
    difference_table.append(table1[0])  # Attach a copy of schema to difference_table because schema would
                                        # not be added below.
    for row in table1:
        if row not in table2:
            difference_table.append(row)

    return difference_table


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    Removes in such a way that the order is kept and later occurrences are removed.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result

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

class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that don't have the same attributes.
    """
    pass

