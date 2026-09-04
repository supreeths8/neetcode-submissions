class TimeMap:

    def __init__(self):
        self._store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._store:
            self._store[key] = []
        self._store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if not self._store.get(key):
            return ""
        
        l = 0
        r = len(self._store[key]) - 1

        the_list = self._store[key]
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if the_list[mid][1] == timestamp:
                return the_list[mid][0]
            elif the_list[mid][1] < timestamp:
                res = the_list[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res


