class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        i, j, m, n = 0, 0, len(word1), len(word2)

        while i < m or j < n:
            if i < m:
                res.append(word1[i])
                i += 1
            if j < n:
                res.append(word2[j])
                j += 1

        return "".join(res)