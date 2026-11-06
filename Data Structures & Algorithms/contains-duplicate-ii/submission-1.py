class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        i, j = 0, 0

        while i < len(nums):
            if nums[i] in window:
                return True

            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[j])
                j += 1

            i += 1

        return False