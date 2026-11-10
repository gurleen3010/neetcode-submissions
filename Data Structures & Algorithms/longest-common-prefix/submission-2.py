class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp= ""

        for i in range(0, len(min(strs, key = len))):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return lcp

            lcp += strs[0][i]
            
        return lcp