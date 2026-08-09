class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums) - 1
        idx = 0
        while idx <= n:
            if nums[idx] == val:
                nums[idx] = nums[n]
                n -= 1
            else:
                idx += 1

        return n + 1