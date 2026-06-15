class Solution(object):
    def containsDuplicate(self, nums):
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = 0

        for i in range(len(nums)):
            if hash[nums[i]] == 1:
                return True
            else:
                hash[nums[i]] += 1

        return False