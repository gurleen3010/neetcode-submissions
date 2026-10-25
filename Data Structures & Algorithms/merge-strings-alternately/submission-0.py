class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        i, j, m, n = 0, 0, len(word1), len(word2)

        while i < m and j < n:
            res.append(word1[i])
            res.append(word2[j])

            i += 1
            j += 1

        while i < m:
            res.append(word1[i])
            i += 1

        while j < n:
            res.append(word2[j])
            j += 1

        return "".join(res)