class Solution:

    def encode(self, strs: List[str]) -> str:

        out = ""
        for word in strs:
            out += str(len(word)) + "#" + word

        print(out)
        return out


    def decode(self, s: str) -> List[str]:
        out = []
        i = 0

        while i < len(s):
            # parse length
            length = 0
            while s[i].isdigit():
                length = length * 10 + int(s[i])
                i += 1

            # skip delimiter '#'
            i += 1

            # extract word
            out.append(s[i:i + length])
            i += length

        return out
