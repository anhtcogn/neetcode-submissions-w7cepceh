class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)        
        longest = 0

        for num in nums:
            if num - 1 not in nset:
                count = 1
                while (num + count) in nset:
                    count += 1
                longest = max(longest, count)
        
        return longest
