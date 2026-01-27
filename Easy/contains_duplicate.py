 Problem:
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
#
# Approach:
# We use a set to store unique elements from the array.
# Since a set does not allow duplicate values, converting the list to a set
# automatically removes duplicates.
#
# If the length of the set is smaller than the length of the original array,
# it means there is at least one duplicate element.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(nums) != len(set(nums))


