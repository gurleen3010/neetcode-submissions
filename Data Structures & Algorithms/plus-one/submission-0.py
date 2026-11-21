class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = (digits[len(digits) - 1] + 1) // 10
        res.append((digits[len(digits) - 1] + 1) % 10)
        i = len(digits) - 2

        while i >= 0 or carry > 0:
            val = (digits[i] if i >= 0 else 0) + carry
            carry = val // 10
            ans = val % 10

            res.append(ans)
            i -= 1

        return list(reversed(res))