class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap={}
        for ch in s:
            hashmap[ch]=hashmap.get(ch,0)+1

        for i in t:
            if i not in hashmap:
                return False
            hashmap[i]-=1

            if hashmap[i]<0:
                return False
        return True