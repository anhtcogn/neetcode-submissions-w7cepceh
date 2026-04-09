class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        two = nums[0]
        one = max(nums[0], nums[1])

        for i in range(2, n):
            tmp = one
            one = max(nums[i] + two, one)
            two = tmp
        
        return one