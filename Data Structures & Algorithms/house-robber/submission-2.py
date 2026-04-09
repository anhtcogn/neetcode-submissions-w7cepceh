class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for i in range(len(nums)):
            tmp = max(nums[i] + one, two)
            one = two
            two = tmp
        
        return two