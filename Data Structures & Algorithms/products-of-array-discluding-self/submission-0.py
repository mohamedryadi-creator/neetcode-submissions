class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        gauche=[1]*n
        droite=[1]*n
        left=1
        right=1
        for i in range(n):
            gauche[i]=gauche[i]*left
            left*=nums[i]
            droite[n-i-1]=droite[n-i-1]*right
            right*=nums[n-i-1]
        res=[1]*n
        for i in range(n):
            res[i]=gauche[i]*droite[i]
        return res

        
        