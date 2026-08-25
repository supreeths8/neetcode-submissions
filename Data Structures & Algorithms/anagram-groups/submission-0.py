class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = {}
        for s in strs:
            sorted_map["".join(sorted(s))] = sorted_map.get("".join(sorted(s)), []) + [s]

        return list(sorted_map.values())


                
