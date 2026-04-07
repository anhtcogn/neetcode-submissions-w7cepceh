class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, r = 0, 0
        max_len = highest_freq = 0

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            highest_freq = max(highest_freq, freq[s[r]])
            number_char_to_replace = r - l - highest_freq + 1
            if number_char_to_replace > k:
                freq[s[l]] -= 1
                l += 1

            max_len = r - l + 1
            r += 1

        return max_len

            
