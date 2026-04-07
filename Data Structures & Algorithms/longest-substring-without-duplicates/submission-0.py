class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = r = 0
        hash_set = set()

        while r < len(s):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
                
            max_len = max(max_len, r - l + 1)
            hash_set.add(s[r])
            r += 1
        
        return max_len