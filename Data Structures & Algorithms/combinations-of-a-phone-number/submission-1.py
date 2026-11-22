class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        result = []

        def letterCombinationsBacktracking(i, currStr):
            if i == len(digits):
                return

            if i == len(digits) - 1:
                key = mapping[digits[i]]
                for k in key:
                    result.append(currStr + k)

            key = mapping[digits[i]]
            for k in key:
                letterCombinationsBacktracking(i + 1, currStr + k)

        letterCombinationsBacktracking(0, "")

        return result