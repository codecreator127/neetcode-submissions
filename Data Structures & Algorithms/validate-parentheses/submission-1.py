class Solution:
    def isValid(self, s: str) -> bool:
        
        opposite_map = {}

        opposite_map["("] = ")"
        opposite_map["{"] = "}"
        opposite_map["["] = "]"



        stack = []

        for i in range(len(s)):
            if len(stack) == 0 or opposite_map[stack[-1]] != s[i]:
                if s[i] not in opposite_map:
                    return False
                
                stack.append(s[i])

            if opposite_map[stack[-1]] == s[i]:
                stack.pop()

        if len(stack) == 0:
            return True

        return False