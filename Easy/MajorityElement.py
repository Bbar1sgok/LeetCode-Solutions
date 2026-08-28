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
        result = 0
        count = 0

        for num in nums:
            # If count drops to 0, pick the current number as the new candidate
            if count == 0:
                result = num

            # Increment if match, otherwise decrement
            if num == result:
                count += 1
            else:
                count -= 1

        return result
