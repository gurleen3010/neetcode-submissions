class Solution:
    def combinationSum_(self, nums: List[int], target: int, result: List[int], finalResult: List[List[int]], idx: int) -> None:
        if target < 0:
            return

        if target == 0:
            smallRes = result.copy()
            finalResult.append(smallRes)
            return

        for i in range(idx, len(nums)):
            result.append(nums[i])
            self.combinationSum_(nums, target - nums[i], result, finalResult, i)
            result.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        finalResult = []

        self.combinationSum_(nums, target, result, finalResult, 0)

        return finalResult