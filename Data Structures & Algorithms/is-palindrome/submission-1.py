class Solution:
    def isAlphaNumeric(self, s: str) -> bool:
        if (s >= 'A' and s <= 'Z') or (s >= 'a' and s <= 'z') or (s >= '0' and s <= '9'):
            return True

        return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        s = s.lower()

        while left < right:
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1

            while left < right and not self.isAlphaNumeric(s[right]):
                right -= 1

            if(s[left] != s[right]):
                return False

            left += 1
            right -= 1

        return True