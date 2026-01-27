# Problem:
# Given a non-empty array of integers where every element appears twice except for one,
# find the element that appears only once.
#
# Approach:
# We use the bitwise XOR operation.
# XOR has the following properties:
# - a ^ a = 0
# - a ^ 0 = a
# - XOR is commutative and associative
#
# By XOR-ing all numbers together, all duplicate elements cancel each other out,
# leaving only the element that appears once.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
  
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            result = 0
            for num in nums:
                result ^= num  
            return result
