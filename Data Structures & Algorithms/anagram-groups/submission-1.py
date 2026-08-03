class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = dict()

        # strings in Python are immutable -> cannot directly sort
        # sorted() : returns list of sorted chars of str

        for s in strs:
            freqMap = [0] * 26
            for ch in s:
                freqMap[ord(ch) - ord('a')] += 1 

            immutable_tuple = tuple(freqMap)

            if immutable_tuple not in mapping:
                mapping[immutable_tuple] = []

            mapping[immutable_tuple].append(s)

        result = list()

        for value in mapping.values():
            result.append(value)

        return result