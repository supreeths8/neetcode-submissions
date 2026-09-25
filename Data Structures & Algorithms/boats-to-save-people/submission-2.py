class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        remain = 0
        count = 0

        while l <= r:
            remain = limit - people[r]
            count += 1

            if remain >= people[l]:
                l += 1
            r -= 1
        return count