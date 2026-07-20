class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1 HashMap + Sorting T : O(n log n) S : O(n)

        # hashmap={}
        # for i in nums:
        #     hashmap[i]=hashmap.get(i,0)+1
        # sorted_freq = sorted(hashmap.items(),key=lambda x:x[1],reverse=True)
        # ans=[]
        # for key,value in sorted_freq[:k]:
        #     ans.append(key)
        # return ans
        
        # Solution 2 Bucket Sort T : O(n) S : O(n)
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for key,value in hashmap.items():
            bucket[value].append(key)
        ans=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                ans.append(num)
            if len(ans)==k:
                return ans


