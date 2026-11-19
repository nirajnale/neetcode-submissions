class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        nextGreater = {}

        for num in nums2:

            while stack and num > stack[-1]:
                nextGreater[stack.pop()] = num

            stack.append(num)

        while stack:
            nextGreater[stack.pop()] = -1

        return [nextGreater[num] for num in nums1]