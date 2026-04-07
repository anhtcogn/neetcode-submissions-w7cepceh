class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        #[-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[i], nums[r], nums[l]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
        #[-4, -1, -1, 0, 1, 2]
