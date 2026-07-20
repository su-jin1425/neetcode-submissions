class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        sorted_freq = sorted(hashmap.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for key,value in sorted_freq[:k]:
            ans.append(key)
        return ans