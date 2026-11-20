import heapq

class KthLargest:

    num = []
    K = 0

    def __init__(self, k: int, nums: List[int]):
        self.num = nums
        self.K = k
        heapq.heapify(self.num)

    def add(self, val: int) -> int:
        heapq.heappush(self.num, val)

        return heapq.nlargest(self.K, self.num)[len(heapq.nlargest(self.K, self.num)) - 1]
