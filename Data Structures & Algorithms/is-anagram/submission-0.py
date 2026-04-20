class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a hashmap to count the num of each char
        # compare the two hashmaps
        # can do in 1 pass

        # early check, if not same len return false

        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        ## s and t must be same len here
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 0
            if t[i] not in dict2:
                dict2[t[i]] = 0

            dict1[s[i]] += 1
            dict2[t[i]] += 1

        return dict1 == dict2