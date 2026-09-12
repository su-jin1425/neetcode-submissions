class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Solution 1 {Array is Sorted} Two Pointer : O(n) S : O(1)
        # if not nums:
        #     return None
        # left=0
        # right=len(nums)-1
        # while left<right:
        #     total=nums[left]+nums[right]
        #     if target==total:
        #         return [left,right]
        #     if target<total:
        #         left+=1
        #     else:
        #         right-=1
             
        # Solution 2 {Array is Not Sorted} HashMap : O(n) S : O(n) 
        if not nums:
            return None
        hashmap={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]]=i
        return None