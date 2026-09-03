class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else :
                dict[i]=1
        
        frequences = [[] for i in range(len(nums) + 1)]
        for n,freq in dict.items() :
            frequences[freq].append(n)
        n=len(nums)
        res=[]
        i=n-1
        while len(res)<k:
            for j in frequences[i]:
                res.append(j)
                if len(res)==k:
                   
                    return res
                 
            i=i-1
        


        