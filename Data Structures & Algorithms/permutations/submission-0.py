class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def permute_(nums: List[int], result: List[int], indexBool: List[bool], length: int) -> None:
            if length == len(nums):
                res.append(result.copy())
                return
            
            for i in range(0, len(nums)):
                if not indexBool[i]:
                    indexBool[i] = True
                    result.append(nums[i])
                    permute_(nums, result, indexBool, length + 1)
                    result.pop()
                    indexBool[i] = False

        permute_(nums, [], [False] * len(nums), 0)
        return res
