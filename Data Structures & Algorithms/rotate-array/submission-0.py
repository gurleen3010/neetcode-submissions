class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        i, j = start, end

        while i < j:
            curr = nums[i]
            nums[i] = nums[j]
            nums[j] = curr

            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)