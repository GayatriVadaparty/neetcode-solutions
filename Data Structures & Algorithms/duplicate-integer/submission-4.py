class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        ## Sorting
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        ## Hash set
        # nums_set = set()
        # for i in range(len(nums)):
        #     if nums[i] in nums_set:
        #         return True
        #     nums_set.add(nums[i])
        # return False

        ## Hash set Length
        return len(nums) != len(set(nums))
        