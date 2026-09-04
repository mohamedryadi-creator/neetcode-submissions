class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1

        eau=0
        while left<right :
            surface = (right-left)*min(heights[left],heights[right])
            eau=max(eau,surface)
            if heights[left]<heights[right]:
                left=left+1
            else :
                right=right-1
        return eau

        