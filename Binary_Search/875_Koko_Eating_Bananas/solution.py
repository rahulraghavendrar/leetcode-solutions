from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maxPile = 0

        for i in piles:
            if i > maxPile:
                maxPile = i

        l = 1
        r = maxPile

        ans = maxPile

        while l <= r:

            midrate = (l + r) // 2

            hours = 0

            for i in piles:
                hours += ceil(i / midrate)

            if hours > h:
                l = midrate + 1

            else:
                ans = midrate
                r = midrate - 1

        return ans