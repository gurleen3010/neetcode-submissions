class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + ((r - l) // 2)

            if nums[mid] <= mid:
                r = mid
            else:
                l = mid + 1

        return nums[l];