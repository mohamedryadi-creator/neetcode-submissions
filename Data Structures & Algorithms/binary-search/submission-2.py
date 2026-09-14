class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right=len(nums)-1
        left=0
        while right>left :
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid
            else :
                left=mid
            if right==left+1:
                if nums[right]==target:
                    return right
                elif nums[left]==target:
                    return left
                else :
                    return -1
        return (nums[left]==target)*left+(nums[left]!=target)*(-1)
        