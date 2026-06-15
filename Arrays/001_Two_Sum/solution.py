class Solution(object):
    def twoSum(self, nums, target):
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = i

        n = target

        for i in range(len(nums)):
            n = n - nums[i]

            if n in hash and hash[n] != i:
                l = [i, hash[n]]
                return l

            else:
                n = target

        return False