class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left, right = 0,len(matrix)-1

        mid= (left + right) // 2

        while left<= right:
            mid= (left + right) // 2
            if target < matrix[mid][0]:
                right=mid-1
            elif target > matrix[mid][-1]:
                left = mid+1

            else:
                break

        if left> right:
            return False
        
        row=mid
        left, right = 0,len(matrix[0])-1

        mid= (left + right) // 2

        while left <= right:
            mid= (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        return False