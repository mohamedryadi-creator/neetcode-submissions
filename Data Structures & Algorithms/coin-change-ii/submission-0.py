class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n+1)]
        for i in range(0,n+1):
            dp[i][0]=1
        for i in range(1,n+1) :
            for k in range(1,amount+1):
                dp[i][k]=dp[i-1][k]
                if k>=coins[i-1]:
                    dp[i][k]+=dp[i][k-coins[i-1]]
        return dp[n][amount]
            
        