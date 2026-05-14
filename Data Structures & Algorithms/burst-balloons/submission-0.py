class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        memo = {}

        def dfs(l, r):

            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            res = 0

            # choose i as last balloon
            for i in range(l, r + 1):

                coins = (
                    nums[l - 1] * nums[i] * nums[r + 1]
                    + dfs(l, i - 1)
                    + dfs(i + 1, r)
                )

                res = max(res, coins)

            memo[(l, r)] = res
            return res

        return dfs(1, n - 2)