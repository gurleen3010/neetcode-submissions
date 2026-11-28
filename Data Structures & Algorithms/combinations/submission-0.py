class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        # n --> 1 to n, k --> numbers present in a list
        def combine_(k: int, res: List[int], val: int, n: int) -> None:
            if k == 0:
                result.append(res.copy())
                return

            for i in range(val, n + 1):
                res.append(i)
                combine_(k - 1, res, i + 1, n)
                res.pop()

        combine_(k, [], 1, n)
        return result