"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res=0

        memo=defaultdict(int)

        for i in intervals:
            memo[i.start]+=1
            memo[i.end]-=1

        memo=dict(sorted(memo.items()))
        curr=0

        for i in memo:
            curr+=memo[i]
            res=max(res,curr)

        return res
