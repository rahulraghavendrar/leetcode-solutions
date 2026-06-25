class Solution(object):
    def longestConsecutive(self, nums):

        seen = set()

        for num in nums:
            seen.add(num)

        result = 0

        for num in seen:

            if num - 1 not in seen:

                length = 1
                current = num

                while current + 1 in seen:
                    current += 1
                    length += 1

                result = max(result, length)

        return result