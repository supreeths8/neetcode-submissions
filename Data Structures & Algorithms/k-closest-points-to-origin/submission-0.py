class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_map = defaultdict(list)

        for p in points:
            key = math.sqrt(p[0]**2 + p[1] ** 2)
            dist_map[key].append(p)

        dist_map_list = list(dist_map.items())
        heapq.heapify(dist_map_list)

        res = []
        for _ in range(len(dist_map_list)):
            if len(res) < k:
                point_map = heapq.heappop(dist_map_list)
                for point in point_map[1]:
                    res.append(point)

        return res
