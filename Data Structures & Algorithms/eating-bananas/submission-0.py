class Solution:
    def speedPileSum(self, piles: List[int], speed: int) -> int:
        sumSpeedHours = 0
        for i in range (0, len(piles)):
            sumSpeedHours += (piles[i] // speed) + (1 if (piles[i] % speed) > 0 else 0)

        return sumSpeedHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)

        left, right = 1, maximum

        while left < right:
            mid = left + ((right - left) // 2)

            sumHours = self.speedPileSum(piles, mid)

            if sumHours > h:
                left = mid + 1
            else:
                right = mid

        return left