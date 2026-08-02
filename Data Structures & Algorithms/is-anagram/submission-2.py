class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqMap1 = [0] * 26;
        freqMap2 = [0] * 26;

        for sChar in s:
            idx = ord(sChar) - ord('a')
            freqMap1[idx] += 1

        for tChar in t:
            idx = ord(tChar) - ord('a')
            freqMap2[idx] += 1    

        for i, value in enumerate(freqMap1):
            if value != freqMap2[i]:
                return False

        return True