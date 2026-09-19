class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxend=[1]*n
        minend=[1]*n
        maxend[0]=nums[0]
        minend[0]=nums[0]
        for i in range(0,n-1):
            maxend[i+1]=max(maxend[i]*nums[i+1],nums[i+1],minend[i]*nums[i+1])
            minend[i+1]=min(maxend[i]*nums[i+1],nums[i+1],minend[i]*nums[i+1])
        return max(maxend)

                

        