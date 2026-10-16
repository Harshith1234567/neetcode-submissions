class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res=0
        prev=intervals[0][1]

        for s,e in intervals[1:]:
            if prev<=s:
                prev=e

            else:
                res+=1
                prev=min(e,prev)

        return res

        