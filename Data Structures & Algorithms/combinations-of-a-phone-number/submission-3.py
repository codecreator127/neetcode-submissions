class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        mapping = {}

        mapping[2] = ["a", "b", "c"]
        mapping[3] = ["d", "e", "f"]
        mapping[4] = ["g", "h", "i"]
        mapping[5] = ["j", "k", "l"]
        mapping[6] = ["m", "n", "o"]
        mapping[7] = ["p", "q", "r", "s"]
        mapping[8] = ["t", "u", "v"]
        mapping[9] = ["w", "x", "y", "z"]

        out = []



        def backtrack(i, string):
            if i == len(digits):
                out.append(string)
                return

            curr = digits[i]
            ## at each step, choose a letter choice
            ## choose current letter at j

            for letter in mapping[int(curr)]:
                backtrack(i + 1, string + letter)

        backtrack(0, "")
        return out