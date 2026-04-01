class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]

        out = [0] * len(temperatures)

        print(out)

        for i in range(1, len(temperatures)):

            print(temperatures[i])
            print(stack[-1][0])

            while stack and temperatures[i] > stack[-1][0]:
                curr = stack.pop()

                out[curr[1]] = (i - curr[1])

            stack.append((temperatures[i], i))

            print(stack);
        
        return out

