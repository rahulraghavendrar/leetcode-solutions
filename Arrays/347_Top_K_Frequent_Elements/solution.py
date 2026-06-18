class Solution(object):
    def topKFrequent(self, nums, k):
        hash = {}
        seen = set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                hash[nums[i]] = 1
                seen.add(nums[i])
            else:
                hash[nums[i]] += 1

        lis = []

        for num, freq in hash.items():
            lis.append([freq, num])

        lis.sort()

        res = []

        while True:
            if k == 0:
                return res
            else:
                a = lis.pop()[1]
                res.append(a)
                k = k - 1