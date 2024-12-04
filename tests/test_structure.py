import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python.structure.src.ExampleClass import ExampleClass as EC

def test_instance_var():
    instance = EC("Test Instance")
    assert instance.instance_var == "Test Instance"

def test_str_method():
    instance = EC("Test Instance")
    assert str(instance) == "ExampleClass with instance_var: Test Instance"

def test_instance_method():
    instance = EC("Test Instance")
    assert instance.instance_method() == "Test Instance"

def test_static_method():
    assert EC.static_method() == "Ich bin eine statische Methode"

def test_class_method():
    assert EC.class_method() == "Ich bin eine Klassenvariable"