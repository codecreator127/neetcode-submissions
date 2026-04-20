class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## use a bucket approach
        ## if we cannot fit the current word into an anagram bucket, create a new one
        ## buckets in the hashmap
        ## use the ord value, but as a representation in the alphabet
        
        buckets = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)
            buckets[key].append(string)
        
        return list(buckets.values())