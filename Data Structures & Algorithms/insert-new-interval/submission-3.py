class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        flag=0
        li=[]
        if not intervals:
            return [newInterval]
        if newInterval[1]<intervals[0][0]:

            li.append(newInterval)
            li.extend(intervals)
            return li

        for x, y in intervals:
            if flag==0:
                if x<=newInterval[0]<= y or x<=newInterval[1]<= y or newInterval[0]<=x<=newInterval[1] or newInterval[0]<=y<=newInterval[1]:
                    li.append([min(newInterval[0],x),max(newInterval[1],y)])
                    flag=1
                elif newInterval[0]<= y:
                    li.append(newInterval)
                    li.append([x,y])
                    flag=1


                else:
                    li.append([x,y])

            else:

                if x<=li[-1][1]:

                    li[-1]=[min(li[-1][0],x),max(li[-1][1],y)]

                else:
                    li.append([x,y])


        if flag==0:
            li.append(newInterval)
            


        return li


        