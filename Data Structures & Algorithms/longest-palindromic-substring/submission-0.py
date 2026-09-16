class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for i in range(n)]
        resinx=0
        reslen=0
        for i in range(n-1,-1,-1):
            for j in range(i,n) :
                if (len(s[i:j])<=2 and s[i]==s[j]) or (dp[i+1][j-1] and s[i]==s[j]):
                    dp[i][j]=True
                    if j-i+1>reslen:
                        reslen=j-i+1
                        resinx=i
        return s[resinx:resinx+reslen]
                    
        
        

        