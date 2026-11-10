class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp, i = "", 0

        for i in range(0, len(min(strs))):
            for j in range(0, len(strs)):
                if j < len(strs) - 1:
                    if strs[j][i] == strs[j + 1][i]:
                        continue
                    else:
                        return lcp
            lcp += strs[0][i]
            
        return lcp