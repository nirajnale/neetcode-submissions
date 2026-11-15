class Solution:
    def maxAscendingSum(self, nums):

        currSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                currSum += nums[i]
            else:
                currSum = nums[i]

            maxSum = max(maxSum, currSum)

        return maxSum