class Solution:
    def subsets_(self, nums: List[int], ans: List[List[int]], smallAns: List[int], idx: int) -> None:
        if idx == len(nums):
            ans.append(smallAns.copy())
            return

        smallAns.append(nums[idx])
        self.subsets_(nums, ans, smallAns, idx + 1)
        smallAns.pop()
        self.subsets_(nums, ans, smallAns, idx + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, smallAns, idx = [], [], 0
        
        self.subsets_(nums, ans, smallAns, idx)

        return ans