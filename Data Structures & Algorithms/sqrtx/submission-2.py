class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1

        while left < right:
            mid = left + ((right - left) // 2)

            sq = mid * mid

            if sq >= x:
                right = mid
            else:
                left = mid + 1

        return left if left * left == x else left - 1