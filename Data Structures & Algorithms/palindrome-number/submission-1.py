class Solution:
    def numDigits(self, x: int) -> int:
        digits = 0
        while x > 0:
            x //= 10
            digits += 1

        return digits

    def reverseNumber(self, x: int) -> int:
        digits = self.numDigits(x)
        reversedNumber = 0

        while x > 0:
            rem = x % 10
            reversedNumber = reversedNumber * 10 + rem
            digits -= 1

            x //= 10

        return reversedNumber

    def isPalindrome(self, x: int) -> bool:
        reversedNum = self.reverseNumber(x)

        return x == reversedNum