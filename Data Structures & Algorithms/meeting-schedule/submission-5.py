"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        memo=defaultdict(int)

        for a in intervals:
            x=a.start
            y=a.end
            memo[x]+=1
            memo[y]-=1

            
        memo =dict(sorted(memo.items()))
        print(memo)

        count=0

        for i in memo:

            count+=memo[i]
            print(i,count)
            if count>1:
                return False

        return True
