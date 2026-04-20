class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## use a bucket approach
        ## if we cannot fit the current word into an anagram bucket, create a new one
        ## buckets in the hashmap
        ## store using the sorted? (k log k to sort)
        
        buckets = {}

        for string in strs:
            sort = "".join(sorted(string))
            if sort not in buckets:
                buckets[sort] = [string]
            else:
                buckets[sort].append(string)
        
        return list(buckets.values())