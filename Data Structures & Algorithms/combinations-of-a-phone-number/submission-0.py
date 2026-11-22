class Solution:
    map = {}
    map['2'] = 'abc'
    map['3'] = 'def'
    map['4'] = 'ghi'
    map['5'] = 'jkl'
    map['6'] = 'mno'
    map['7'] = 'pqrs'
    map['8'] = 'tuv'
    map['9'] = 'wxyz'

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        if len(digits) == 1:
            key = self.map[digits]
            result = []
            for val in key:
                result.append(val)

            return result

        currentDigit = digits[0]
        restDigits = digits[1:]
        key = self.map[currentDigit]

        res = self.letterCombinations(restDigits)
        finalResult = []

        for val in key:
            for r in res:
                finalResult.append(val + r)

        return finalResult
