class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1=len(text1)
        n2=len(text2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        dp[0][0]=0
        for i in range(0,n1):
            for j in range(0,n2):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=max(dp[i][j]+1,dp[i][j+1],dp[i+1][j])
                else :
                    dp[i+1][j+1]=max(dp[i][j],dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]
                

        