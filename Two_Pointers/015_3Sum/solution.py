class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []

        for i in range(len(nums)):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            seen = set()

            while l < r:

                if l == i:
                    l += 1
                    continue

                if r == i:
                    r -= 1
                    continue

                currsum = nums[i] + nums[l] + nums[r]

                if currsum < 0:
                    l += 1

                elif currsum > 0:
                    r -= 1

                else:
                    x = sorted([nums[i], nums[l], nums[r]])
                    t = tuple(x)

                    if t not in seen:
                        result.append([nums[i], nums[l], nums[r]])
                        seen.add(t)

                    l += 1
                    r -= 1

        return result