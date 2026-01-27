class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return len(nums) != len(set(nums))

