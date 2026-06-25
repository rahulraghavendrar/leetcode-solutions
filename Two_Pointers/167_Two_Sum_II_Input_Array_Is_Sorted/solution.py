class Solution(object):
    def twoSum(self, numbers, target):
        currsum = 0
        l = 0
        r = len(numbers) - 1

        while l < r:

            currsum = numbers[l] + numbers[r]

            if currsum > target:
                r -= 1

            elif currsum < target:
                l += 1

            else:
                return [l + 1, r + 1]