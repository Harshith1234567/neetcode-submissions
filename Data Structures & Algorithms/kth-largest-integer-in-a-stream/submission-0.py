class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.li,self.k=nums,k

        heapq.heapify(self.li)
        while len(self.li)>k:
            heapq.heappop(self.li)

    def add(self, val: int) -> int:

        heapq.heappush(self.li,val)
        if len(self.li)>self.k:
            heapq.heappop(self.li)

        return self.li[0]

        
