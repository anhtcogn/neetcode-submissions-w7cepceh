class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
        
        longest = 0
        for i in range(len(nums)):
            count = 0
            if hash_map.get(nums[i] - 1, 0) == 0:
                mark = nums[i]
                while hash_map.get(mark, 0) != 0:
                    count += 1
                    mark += 1
                longest = max(longest, count)
        
        return longest
