class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            print(stack)
            if o == "C":
                if stack:
                    stack.pop()
            elif o == "+":
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(o))
            
        print(stack)
        return sum(stack)