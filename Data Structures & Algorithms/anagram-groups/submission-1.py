class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = defaultdict(list)

        for s in strs:
            sorted_map["".join(sorted(s))].append(s)
        
        return list(sorted_map.values())