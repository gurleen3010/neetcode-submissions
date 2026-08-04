class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = []
        for s in strs:
            # encoding.append(str(len(s)) + "#" + s)
            encoding.append(f"{len(s)}#{s}")

        return "".join(encoding)

    def decode(self, s: str) -> List[str]:
        idx = 0
        result = []
        while(idx < len(s)):
            j = idx
            while(j < len(s) and s[j] != '#'):
                j += 1

            length = int(s[idx:j])

            word = s[j + 1 : j + 1 + length]

            result.append(word)

            idx = j + 1 + length

        return result

