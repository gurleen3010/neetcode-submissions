import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for point in points:
            x = point[0]
            y = point[1]

            dist = (x*x + y*y)

            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        answer = []

        while len(heap) > 0:
            coordinate = heapq.heappop(heap)
            answer.append([coordinate[1],coordinate[2]])

        return answer