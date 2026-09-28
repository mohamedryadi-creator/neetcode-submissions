class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[float('inf')]*n
        dp[-1]=0
        for i in range(n-2,-1,-1):
            sautmax=nums[i]
            for j in range(sautmax+1):
                if i+j<n:
                    dp[i]=min(1+dp[i+j],dp[i])
        return dp[0]
        