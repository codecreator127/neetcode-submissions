class Solution:
    def checkValidString(self, s: str) -> bool:
        
        ## use a stack

        starStack = []
        stack = []

        for i, c in enumerate(s):
            print(i, c)

            if c == "(":
                stack.append((c, i))
            elif c == "*":
                starStack.append((c, i))

            else:
                if stack:
                    stack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False

        print(stack)
        print(starStack)

        while stack:
            if starStack and starStack[-1][1] > stack[-1][1]:
                stack.pop()
                starStack.pop()
            else:
                return False

        return True