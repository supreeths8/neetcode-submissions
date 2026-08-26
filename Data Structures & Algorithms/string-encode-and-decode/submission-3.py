class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded = ""
        for st in strs:
            encoded += str(len(st)) + ','
        encoded += '#' + "".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = []
        res = []
        i = 0
        
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            print(sizes)
            sizes.append(int(s[i:j]))
            i = j + 1
        
        i += 1
        for size in sizes:
            res.append(s[i:i + size])
            i += size
        
        return res


        


        
        
