class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        total = 0

        for o in operations:
            print(stack)
            if o == "C":
                if stack:
                    total -= stack.pop()
            elif o == "+":
                total += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                total += stack[-1]*2
                stack.append(stack[-1]*2)
            else:
                stack.append(int(o))
                total += int(o)
            
        return total