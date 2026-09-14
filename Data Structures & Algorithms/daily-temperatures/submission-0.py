class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)) :
            tempact=temperatures[i]
            while len(stack)>0 and tempact>temperatures[stack[-1]]:
              
                j=stack.pop()
                result[j]=i-j


            stack.append(i)
        return result
            
            


        