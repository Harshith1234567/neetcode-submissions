class Solution:
    def trap(self, height: List[int]) -> int:
        i, j=0, 0
        li=[]
        count=0
        while j<len(height) and i<len(height):
            if height[i] ==0 :
                i+=1
                continue
                
            if height[j] == 0 or i==j or j<i:
                j+=1
                continue
            
            if height[i] > height[j]:
                j+=1
                continue

            area = ((j-i-1) * min(height[i] , height[j])) - sum(height[i+1:j] )
            print(i,j,area)
            li.append((j,i))
            count+=area
            i=j
            j+=1


        i, j=len(height)-1, len(height)-1
        
        while j>=0 and i>=0:
            print(i,j)
            if height[i] ==0 :
                i-=1
                continue
            if (i,j) in li: 
                i=j
                j-=1 
            if height[j] == 0 or i==j or j>i :
                j-=1
                continue
            
            if height[i] > height[j] :
                j-=1
                continue

            area = ((i-j-1) * min(height[i] , height[j])) - sum(height[j+1:i] )
            print(i,j,area)
            count+=area
            i=j
            j-=1

        return count
        