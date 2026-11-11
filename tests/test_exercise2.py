import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing_grade_five():
    assert is_passing(5) is True


# bug report 2
def test_r2_is_valid_password_exact_eight_chars_with_digit():
    assert is_valid_password("abcdefgh1") is True


# bug report 3
def test_r3_clamp_below_low():
    assert clamp(2, 5, 10) == 5
