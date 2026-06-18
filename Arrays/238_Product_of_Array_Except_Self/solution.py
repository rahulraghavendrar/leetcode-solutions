class Solution(object):
    def productExceptSelf(self, nums):
        pre = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        suf = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= suf
            suf *= nums[i]

        return res