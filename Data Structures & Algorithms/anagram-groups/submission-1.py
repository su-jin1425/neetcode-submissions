class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution Default Dict {HashMap} T : O(n × k log k) S : O(n × k)
        from collections import defaultdict
        hashmap=defaultdict(list)
        for i in range(len(strs)):
            key="".join(sorted(strs[i]))
            hashmap[key].append(strs[i])

        return list(hashmap.values())