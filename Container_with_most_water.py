class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0

        while start < end:
            h = height[start] if height[start] < height[end] else height[end]
            w = end - start
            area = h * w if h * w > area else area

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return area
