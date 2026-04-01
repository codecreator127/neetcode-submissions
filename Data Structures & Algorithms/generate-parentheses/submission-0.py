class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ## use a stack for parenthesis
        ## can probably brute force this

        out = []

        ## 2 choices
        ## add a ( or add a )

        def backtrack(openB, closeB, brackets):
            if closeB > openB:
                return

            if openB + closeB == 2*n:
                if openB == closeB:
                    out.append(brackets)
                return

            ### choice 1 add a ( to the string
            backtrack(openB + 1, closeB, brackets + "(")

            ### choice 2 add a ) to the string
            backtrack(openB, closeB + 1, brackets + ")")


        backtrack(0, 0, "")

        return out

            