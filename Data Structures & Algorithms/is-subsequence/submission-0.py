class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        scount = 0
        tcount = 0
        
        while scount < len(s) and tcount < len(t):
            if s[scount] == t[tcount]:
                scount += 1
            
            tcount += 1

        return scount == len(s)
        