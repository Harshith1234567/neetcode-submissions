"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #return 0


        dics=defaultdict(int)
        dice=defaultdict(int)
        for inter in intervals:
            dics[inter.start]+=1
            dice[inter.end-1]-=1
        count=0
        res=0
        items=list(dics.items()) + list(dice.items())
        #items=list(sorted(dics.items(),key=lambda x:x[0])) + list(sorted(dice.items(),,key=lambda x:x[0]))
        items.sort(key=lambda  x:x[0])
        print(items)
        for k,v in items:
            count+=v
            res=max(res,count)

        return res
