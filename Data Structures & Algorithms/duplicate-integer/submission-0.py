class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) and set(nums) != nums else False
        