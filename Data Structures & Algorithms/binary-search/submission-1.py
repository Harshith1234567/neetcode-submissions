class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid= (right+left)//2
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left


        #print(mid)

        while nums[mid] != target:

            if left == right or left == mid or right == mid or left >= right:
                break

            if target<mid:
                right=mid-1
                if nums[right] == target:
                    return right
                mid= (right+left)//2

            else:
                left=mid+1
                if nums[left] == target:
                    return left
                mid= (right+left)//2

            
            if left == right or left == mid or right == mid or left >= right:
                break


        if nums[mid]== target:
            return mid
        return -1



        