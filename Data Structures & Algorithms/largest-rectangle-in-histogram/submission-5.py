class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        li=[]

        maxrec=0

        for i,ele in enumerate(heights):
            s=i
            while li and li[-1][1] > ele:
                idx,h=li.pop()

                maxrec=max(maxrec, (i-idx)*h)
                s=idx
            
            li.append([s,ele])


        for i,h in li:
            maxrec=max(maxrec, h * (len(heights)-i))

        return maxrec