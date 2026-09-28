class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False]*n
        dp[-1]=True
        for i in range(n-2,-1,-1):
            sautmax=nums[i]
            for j in range(sautmax+1):
                if i+j<n and dp[i+j]:
                    dp[i]=True
                    break
        return dp[0]
                    

        


        