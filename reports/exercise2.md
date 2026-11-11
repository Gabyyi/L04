# Bug reports for exercise2.py

Line: 3
Problem: Incorrect comparison operator; the function should return True when the grade is 5 or more, but uses `grade > 5` which excludes grade 5.
Example: is_passing(5) returns False, but it should return True.
Fix: return grade >= 5

Line: 8
Problem: Incorrect length validation; the function requires at least 8 characters, but uses `len(password) > 8` which excludes exactly 8 characters.
Example: is_valid_password("abcdefgh") returns False, but it should return True since it has exactly 8 characters and contains a digit (e.g., 'a1bcdefg').
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 13
Problem: Incorrect min() and max() usage; the function should clamp x between low and high, but uses `min(x, low)` which incorrectly limits x to below or equal to low, not to high.
Example: clamp(10, 5, 15) returns 5, which is correct, but clamp(3, 5, 15) returns 3, which is below low and should be clamped to 5.
Example: clamp(2, 5, 10) returns 2, but should return 5.
Fix: return max(low, min(x, high))
