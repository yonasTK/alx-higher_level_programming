#!/usr/bin/python3
"""
Provides a function to find a peak element in an unsorted list of integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in an unsorted list of integers
    """
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return list_of_integers[0] if list_of_integers[0] > list_of_integers[1] else list_of_integers[1]
    midpoint = len(list_of_integers) // 2
    if list_of_integers[midpoint] < list_of_integers[midpoint - 1]:
        return find_peak(list_of_integers[:midpoint])
    if list_of_integers[midpoint] < list_of_integers[midpoint + 1]:
        return find_peak(list_of_integers[midpoint + 1:])
    return list_of_integers[midpoint]
