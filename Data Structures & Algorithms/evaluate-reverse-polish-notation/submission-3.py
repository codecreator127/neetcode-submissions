class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        import math

        stack = []

        for token in tokens:

            print(token)

            if token == "+":
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(num1 + num2)
            elif token == "-":
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(num1 - num2)
            elif token == "*":
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(num1 * num2)
            elif token == "/":
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(int(num1/num2))
            else:        
                stack.append(int(token))
        
            print(stack)

        return stack[0]