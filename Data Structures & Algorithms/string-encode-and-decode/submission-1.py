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
            length_str = []
            while(idx < len(s) and s[idx] != '#'):
                length_str.append(s[idx])
                idx += 1

            # to move one position more for #
            idx += 1

            final_length = int("".join(length_str)) # convert into number

            decoded_string = []
            while(idx < len(s) and final_length > 0):
                decoded_string.append(s[idx])
                final_length -= 1
                idx += 1

            result.append("".join(decoded_string))

        return result

