# Bug reports for exercise1.py

Line: 3
Problem: The condition `n % 2 == 1` checks if a number is odd, not even. For even numbers, the remainder when divided by 2 should be 0, not 1.
Example: `is_even(4)` returns `False` when it should return `True` because 4 is even and 4 % 2 == 0, not 1.
Fix: Change `n % 2 == 1` to `n % 2 == 0`

Line: 8
Problem: The function `rectangle_area` incorrectly returns the sum of width and height instead of the product (area of a rectangle).
Example: `rectangle_area(5, 3)` returns `8`, but the correct area should be `15`.
Fix: Change `return width + height` to `return width * height`

Line: 13
Problem: The function `double(n)` adds 2 to `n`, but it should return twice the number (i.e., `n * 2`).
Example: `double(3)` returns `5`, but it should return `6`.
Fix: Change `return n + 2` to `return n * 2`
