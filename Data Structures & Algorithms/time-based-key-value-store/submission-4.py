from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.memo=defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memo[key][timestamp]=value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.memo:
            return ''

        time=self.memo[key]

        idx=time.bisect_right(timestamp) - 1

        if idx >= 0:
            closest_time = time.iloc[idx]
            return time[closest_time]
        return ""


        

        
