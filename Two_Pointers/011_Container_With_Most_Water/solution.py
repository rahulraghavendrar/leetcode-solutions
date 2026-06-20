class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0

        while left < right:

            length = min(height[left], height[right])
            breadth = right - left

            currarea = length * breadth

            if maxarea < currarea:
                maxarea = currarea

            if height[left] > height[right]:
                right -= 1

            elif height[right] > height[left]:
                left += 1

            else:
                if height[left + 1] > height[right - 1]:
                    left += 1
                elif height[left + 1] < height[right - 1]:
                    right -= 1
                else:
                    left += 1
                    right -= 1

        return maxarea