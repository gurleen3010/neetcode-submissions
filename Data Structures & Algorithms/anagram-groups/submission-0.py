class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = dict()

        # strings in Python are immutable -> cannot directly sort
        # sorted() : returns list of sorted chars of str

        for s in strs:
            s_sorted = "".join(sorted(s))

            if s_sorted not in mapping:
                mapping[s_sorted] = []

            mapping[s_sorted].append(s)

        result = list()

        for value in mapping.values():
            result.append(value)

        return result