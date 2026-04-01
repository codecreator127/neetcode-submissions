class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]

        out = [0] * len(temperatures)

        for i in range(1, len(temperatures)):

            while stack and temperatures[i] > stack[-1][0]:
                curr = stack.pop()

                out[curr[1]] = (i - curr[1])

            stack.append((temperatures[i], i))

        return out

