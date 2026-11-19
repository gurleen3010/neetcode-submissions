class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        # add things to set
        for num in nums:
            seen.add(num)

        maxConsecutiveLength = 0
        consecutiveLength = 0
        for num in nums:
            while (num - 1) in seen:
                num = num - 1

            while num in seen:
                consecutiveLength += 1
                seen.remove(num)
                num += 1

            maxConsecutiveLength = max(maxConsecutiveLength, consecutiveLength)
            consecutiveLength = 0

        return maxConsecutiveLength