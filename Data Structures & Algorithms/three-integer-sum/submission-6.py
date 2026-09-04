class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res=[]
        if len(nums)==3 and nums[0]+nums[1]+nums[2]==0 :
            return [nums]
        else :
            for i in range(len(nums)-3) :
                left=i+1
                right=len(nums)-1
                
                while left<right:
                    sum=nums[left]+nums[right]+nums[i]
                    if sum==0:
                        liste=[nums[i],nums[left],nums[right]]
                        if liste not in res:
                            res.append(liste)
                        left+=1
                        right-=1
                    elif sum>0 :
                        right=right-1
                    elif sum <0:
                        left+=1
            return res

            
            


            
        