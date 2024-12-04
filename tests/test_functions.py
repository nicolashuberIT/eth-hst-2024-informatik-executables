import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python.functions import global_var, my_function
from python.functions import get_global_var, set_global_var

def test_my_function_default():
    set_global_var(20)  # global_var vor dem Test zurücksetzen
    result = my_function(5)
    assert result == 5
    assert get_global_var() == 2

def test_my_function_custom():
    set_global_var(20)  # global_var vor dem Test zurücksetzen
    result = my_function(5, 10)
    assert result == 5
    assert get_global_var() == 10