class Solution:    
    def minWindow(self, s: str, t: str) -> str:

        def checkIncludeSub(dict1, dict2) -> bool:
        ## check if dict1 is in dict2

            for key in dict1:
                if key not in dict2:
                    return False
                if dict1[key] > dict2[key]:
                    return False
            
            return True
        
        ## key observation: if t is within a substring of s
        ## including duplicates -> must use seen dict

        if len(t) > len(s):
            return ""

        if len(t) == 1:
            if t in s:
                return t
            return ""

        t_dict = {}

        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1

        s_dict = {}
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1


        print(t_dict)

        left = 0
        seen = {}
        out = s

        for right in range(len(s)):
            char = s[right]
            seen[char] = seen.get(char, 0) + 1

            print(seen)

            while checkIncludeSub(t_dict, seen):

                if len(out) > len(s[left:right + 1]):
                    out = s[left:right + 1]
                
                print(out)

                leftChar = s[left]

                seen[leftChar] -= 1
                left += 1

        if checkIncludeSub(t_dict, s_dict):
            return out
            
        return ""
