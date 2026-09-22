class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)

        if abs(target) > s:
            return 0

        width = 2 * s + 1
        dp = [[0] * width for _ in range(n + 1)]


        dp[0][s] = 1

        for i in range(1, n + 1):
            num = nums[i - 1]

            for j in range(width):
              
                if 0 <= j - num < width:
                    dp[i][j] += dp[i - 1][j - num]

                
                if 0 <= j + num < width:
                    dp[i][j] += dp[i - 1][j + num]

        return dp[n][target + s]