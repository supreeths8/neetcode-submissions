class MyHashSet:

    def __init__(self):
        self._data = [False for _ in range(1000001)]

    def add(self, key: int) -> None:
        self._data[key] = True
        

    def remove(self, key: int) -> None:
        self._data[key] = False
        

    def contains(self, key: int) -> bool:
        return self._data[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)