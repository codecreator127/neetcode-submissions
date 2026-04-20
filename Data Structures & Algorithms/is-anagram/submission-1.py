class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a hashmap to count the num of each char
        # just use defaultdict for 0
        # can do in 1 pass

        # early check, if not same len return false

        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1

        return all(v == 0 for v in count.values())