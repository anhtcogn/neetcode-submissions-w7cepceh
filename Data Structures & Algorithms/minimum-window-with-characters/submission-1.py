class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_map = {}
        for i in t:
            target_map[i] = target_map.get(i, 0) + 1

        have, need = 0, len(target_map)
        res, res_len = [-1, -1], float("inf")
        window_map = {}
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_map[char] = window_map.get(char, 0) + 1

            if char in target_map and window_map[char] == target_map[char]:
                have += 1

            while have == need:
                # update res and res_len
                if res_len > (r - l + 1):
                    res_len = r - l + 1
                    res = [l, r]

                # remove left char/shrink window
                left_char = s[l]
                window_map[left_char] -= 1

                if left_char in target_map and window_map[left_char] < target_map[left_char]:
                    have -= 1
                
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""

