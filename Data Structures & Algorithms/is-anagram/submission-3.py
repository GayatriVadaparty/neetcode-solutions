class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        ## Sorting
        # return sorted(s) == sorted(t)

        ## Hash Map
        countS, countT = {},{}
        for i in range(len(s)): #both same length
            countS[s[i]]= 1+ countS.get(s[i],0) #handles if key doesn't exist
            countT[t[i]]= 1+ countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c): #handles keyerror
                return False
        return True



        