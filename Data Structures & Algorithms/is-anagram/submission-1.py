class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if len(s) == len(t) and sorted(s) == sorted(t) else False
        