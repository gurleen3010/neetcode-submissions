class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = list()
        leftProd.append(1)
        rightProd = list()
        rightProd.append(1)

        lProd = 1;
        for num in nums:
            lProd *= num
            leftProd.append(lProd)

        rProd = 1;
        for idx in range(len(nums) - 1, -1, -1):
            rProd *= nums[idx]
            rightProd.append(rProd)

        rightProd.reverse()

        result = list()

        for idx in range(len(nums)):
            result.append(leftProd[idx] * rightProd[idx + 1])

        return result