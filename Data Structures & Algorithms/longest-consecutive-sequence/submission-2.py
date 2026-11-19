class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        maxConsecutiveLength = 0
        
        for num in nums:
            if (num - 1) not in seen:
                consecutiveLength = 0
                while num in seen:
                    consecutiveLength += 1
                    seen.remove(num)
                    num += 1

                maxConsecutiveLength = max(maxConsecutiveLength, consecutiveLength)

        return maxConsecutiveLength