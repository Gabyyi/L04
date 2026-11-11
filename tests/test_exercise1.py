import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even_returns_true_for_even_numbers():
    assert is_even(4) is True
    assert is_even(6) is True
    assert is_even(0) is True
    assert is_even(2) is True


# bug report 2
def test_r2_rectangle_area_returns_correct_area():
    assert rectangle_area(5, 3) == 15


# bug report 3
def test_r3_double_function_returns_twice_the_number():
    assert double(5) == 10
