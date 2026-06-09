class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ## Counter - only python
        # return Counter(s) == Counter(t)

        ## Sorting
        # return sorted(s) == sorted(t)

        ## Hash Map
        # countS, countT = {},{}
        # for i in range(len(s)): #both same length
        #     countS[s[i]]= 1+ countS.get(s[i],0) #handles if key doesn't exist
        #     countT[t[i]]= 1+ countT.get(t[i],0)
        # for c in countS:
        #     if countS[c] != countT.get(c): #handles keyerror
        #         return False
        # return True

        ## Hash Table
        arr = [0]*26
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')]+=1
            arr[ord(t[i]) - ord('a')]-=1
        for val in arr:
            if val!=0:
                return False
        return True



        