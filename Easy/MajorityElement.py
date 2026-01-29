# Problem:
# Find the element that appears more than n/2 times in the array.
#
# Approach:
# Boyer-Moore Voting Algorithm
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
