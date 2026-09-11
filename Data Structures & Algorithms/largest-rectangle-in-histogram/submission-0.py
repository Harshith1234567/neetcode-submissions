class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxrec=0
        for i,ele in enumerate(heights):
            if len(stack)==0 or stack[-1][1] <= ele:
                stack.append([i,ele])
            else:
                idx=i
                while len(stack) and stack[-1][1]>ele:
                    idx,h=stack.pop()
                    if maxrec < (i-idx)*h:
                        maxrec = (i-idx)*h
                
                stack.append([idx,ele])

        print(stack)
        for i,h in stack:
            if maxrec < (len(heights)-i)*h:
                maxrec = (len(heights)-i)*h

        return maxrec


        