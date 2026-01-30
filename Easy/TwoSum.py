class Solution(object):
    def twoSum(self, nums, target):
        """
        Problem:
        Given an array of integers nums and an integer target,
        return the indices of the two numbers such that they add up to target.

        Approach:
        - Use a dictionary (hash map) to store previously seen numbers
          along with their indices.
        - For each number, calculate the value needed to reach the target.
        - If the needed value exists in the dictionary, return the indices.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i
