class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n+2)]
        dp[-1][1]=0
        dp[-1][0]=0
        
        for i in range(n-1,-1,-1):
            for allowed in [True,False]:
                if allowed :
                    dp[i][1]=max(dp[i+1][1],dp[i+1][0]-prices[i])
                else :
                    dp[i][0]=max(dp[i+2][1]+prices[i],dp[i+1][0])
        return dp[0][1]


            

        
        