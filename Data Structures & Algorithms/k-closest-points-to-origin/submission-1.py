class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points = [ [(x**2+y**2) ** 0.5,[x,y]  ] for x, y in points]
        print (points)

        heapq.heapify(points)


        return [ heapq.heappop(points)[1] for x in range(k)]

