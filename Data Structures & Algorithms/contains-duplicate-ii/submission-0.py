class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums)):
            j = i + 1
            if j > len(nums):
                return False

            while j < len(nums) and (j - i) <= k:
                if nums[i] == nums[j]:
                    return True
                j += 1

        return False