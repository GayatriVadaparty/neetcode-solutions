class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #Iterative (2 pass)
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        