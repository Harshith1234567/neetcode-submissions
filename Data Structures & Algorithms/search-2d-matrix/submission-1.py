class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix) # 3
        n=len(matrix[0]) # 4
        l=0
        r=(m*n)-1

        while l<=r:
            mid=l+((r-l)//2)
            tr=mid//n   # 1
            tc=mid% n    #0
            if matrix[tr][tc]==target:
                return True

            if matrix[tr][tc]>target:
                r=mid-1

            else:
                l=mid+1

        return False
        