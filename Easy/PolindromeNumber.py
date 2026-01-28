# Problem:
# Given an integer x, return True if x is a palindrome, and False otherwise.
#
# A palindrome number reads the same backward as forward.
#
# Examples:
# 121  -> True
# -121 -> False
# 10   -> False
#
# Approach:
# 1. Convert the integer to a string.
# 2. Reverse the string using slicing.
# 3. Compare the original string with the reversed string.
#    - If they are equal, the number is a palindrome.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of digits in the number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert integer to string
        x = str(x)

        # Reverse the string
        reversed_x = x[::-1]

        # Check if the original and reversed strings are equal
        if x == reversed_x:
            return True
        else:
            return False
