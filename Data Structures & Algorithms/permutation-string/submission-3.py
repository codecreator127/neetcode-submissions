class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ### check if len(smaller string) inside bigger string
        ### and check if seen[] == smaller_dict

        if len(s1) > len(s2):
            return False

        smaller = s1
        larger = s2

        if len(s2) < len(s1):
            larger = s1
            smaller = s2

        smaller_dict = {}

        for i in range(len(smaller)):
            smaller_dict[smaller[i]] = smaller_dict.get(smaller[i], 0) + 1

        
        print(smaller_dict)


        left = 0

        seen = {}
        for right in range(len(larger)):

            seen[larger[right]] = seen.get(larger[right], 0) + 1

            if (right - left + 1) == len(smaller):
                if seen == smaller_dict:
                    return True
                seen[larger[left]] -= 1
                if seen[larger[left]] == 0:
                    del seen[larger[left]]

                left += 1
        
        return False