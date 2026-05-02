class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_map = {}

        for i in s:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        for j in t:
            if j not in hash_map :
                return False
            else:
                hash_map[j] -= 1
        
        for number in hash_map:
            if hash_map[number] > 0:
                return False


        
        return True
        