class Solution:
    def maxArea(self, heights: List[int]) -> int:
         max_area = 0
         i = 0
         x = len(heights) - 1
         while i < x:
             wid = x - i
             height = min(heights[i],heights[x])
             max_area = max((wid*height), max_area)
             if heights[i] == height:
                 i += 1
             else:
                 x -= 1

         return max_area                   
