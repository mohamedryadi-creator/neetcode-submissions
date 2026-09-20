class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*len(nums)
        dp[-1]=1

        for i in range(n-2,-1,-1):
            for j in range(i,n):
                if nums[j]>nums[i]:
                    dp[i]=max(dp[j],dp[i])
            dp[i]+=1
        return max(dp)
            


        
            
            

        