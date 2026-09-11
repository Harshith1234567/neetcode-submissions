"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x:(x.start,x.end))
        if intervals==[]:
            return True

        prev=intervals[0]

        for inter in intervals[1:]:
            if inter.start<prev.end<=inter.end or prev.start<=inter.start<prev.end:
                return False

            prev=inter

        return True