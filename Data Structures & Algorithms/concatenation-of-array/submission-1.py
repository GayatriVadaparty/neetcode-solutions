class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ## Iterative (2 pass)
        # ans = []
        # for i in range(2):
        #     for n in nums:
        #         ans.append(n)
        # return ans

        ## Iterative (1 pass)
        ans = [0]*2*len(nums)
        for i in range(len(nums)):
            ans[i]= ans[i+len(nums)] = nums[i]
        return ans


        