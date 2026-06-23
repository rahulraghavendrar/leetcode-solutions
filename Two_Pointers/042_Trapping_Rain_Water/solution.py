class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftmax = height[left]
        rightmax = height[right]

        result = 0

        while left < right:

            if leftmax < rightmax:

                left += 1

                leftmax = max(height[left], leftmax)

                if leftmax - height[left] < 0:
                    result += 0
                else:
                    result += (leftmax - height[left])

            else:

                right -= 1

                rightmax = max(height[right], rightmax)

                if rightmax - height[right] < 0:
                    result += 0
                else:
                    result += (rightmax - height[right])

        return result