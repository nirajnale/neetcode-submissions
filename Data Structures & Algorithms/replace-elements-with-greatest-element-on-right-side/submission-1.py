class Solution:
    def replaceElements(self, arr):

        maxRight = -1

        for i in range(len(arr) - 1, -1, -1):

            temp = arr[i]

            arr[i] = maxRight

            maxRight = max(maxRight, temp)

        return arr