class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # stores indices
        max_area = 0
        
        heights.append(0)  # sentinel to flush stack
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                
                # width calculation
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area