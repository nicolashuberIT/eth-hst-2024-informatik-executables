import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.search import binary_search, linear_search
from algorithms.sort import bubble_sort_asc, bubble_sort_desc

def test_bubble_sort_asc():
    assert bubble_sort_asc([64, 34, 25, 12]) == [12, 25, 34, 64]
    assert bubble_sort_asc([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert bubble_sort_asc([]) == []
    assert bubble_sort_asc([1]) == [1]
    assert bubble_sort_asc([2, 1]) == [1, 2]
    assert bubble_sort_asc([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_desc():
    assert bubble_sort_desc([64, 34, 25, 12]) == [64, 34, 25, 12]
    assert bubble_sort_desc([5, 1, 4, 2, 8]) == [8, 5, 4, 2, 1]
    assert bubble_sort_desc([]) == []
    assert bubble_sort_desc([1]) == [1]
    assert bubble_sort_desc([2, 1]) == [2, 1]
    assert bubble_sort_desc([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]

def test_linear_search():
    assert linear_search([64, 34, 25, 12], 25) == 2
    assert linear_search([5, 1, 4, 2, 8], 4) == 2
    assert linear_search([], 1) == -1
    assert linear_search([1], 1) == 0
    assert linear_search([2, 1], 1) == 1
    assert linear_search([1, 2, 3, 4, 5], 6) == -1

def test_binary_search():
    assert binary_search([12, 25, 34, 64], 25) == 1
    assert binary_search([1, 2, 4, 5, 8], 4) == 2
    assert binary_search([], 1) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1, 2], 2) == 1
    assert binary_search([1, 2, 3, 4, 5], 6) == -1