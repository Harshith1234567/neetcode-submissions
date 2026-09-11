class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1

        while i<j:
            su=numbers[i]+numbers[j]
            if target == su:
                return [i+1,j+1]
            if su > target:
                j-=1
            else:
                i+=1


        