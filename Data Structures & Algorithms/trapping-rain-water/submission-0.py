class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxleft=height[left]
        maxright=height[right]
        eau=0
        while right>left :
            if height[left]>=height[right]:
                right=right-1
                if height[right]>maxright :
                    maxright=height[right]
                else :
                    eau+=min(maxleft,maxright)-height[right]
            else :
                left=left+1
                if height[left]>maxleft:
                    maxleft=height[left]
                else :
                    eau+=min(maxleft,maxright)-height[left]
        return eau



        