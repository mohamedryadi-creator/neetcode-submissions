class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        target=0
        for num in nums:
            target+=num
        if target%2!=0:
            return False
        target=target//2
        dp=[False]*(target+1)
        dp[0]=True
        for num in nums:
            previous=dp.copy()
            for i in range(num,target+1):
                dp[i]=(previous[i] or previous[i-num])
        return dp[-1]
            


        