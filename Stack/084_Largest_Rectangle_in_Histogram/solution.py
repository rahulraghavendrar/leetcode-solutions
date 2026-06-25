class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxarea = 0

        for i, j in enumerate(heights):

            newh = i

            while stack and j < stack[-1][1]:

                l, m = stack.pop()

                width = i - l
                area = m * width

                if area > maxarea:
                    maxarea = area

                newh = l

            stack.append([newh, j])

        while stack:

            l, m = stack.pop()

            width = len(heights) - l
            area = m * width

            if area > maxarea:
                maxarea = area

        return maxarea