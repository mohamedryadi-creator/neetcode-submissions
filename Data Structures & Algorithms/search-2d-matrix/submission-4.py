class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up=0
        down=len(matrix)-1

        while down>up :
            midligne=(down+up)//2
            if matrix[midligne][0]==target :
                return True
            elif matrix[midligne][0]>target :
                down=midligne-1
            else :
                up=midligne+1
        if matrix[up][0]>target :
            up=up-1
        left=0
        right=len(matrix[0])-1
        while left<=right:
            midcolonne=(left+right)//2
            if matrix[up][midcolonne]==target:
                return True
            elif matrix[up][midcolonne]>target:
                right=midcolonne-1
            else :
                left=midcolonne+1
        return False

        