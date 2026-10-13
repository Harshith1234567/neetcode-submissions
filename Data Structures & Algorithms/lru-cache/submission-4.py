class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity

        self.memo=OrderedDict()
        

    def get(self, key: int) -> int:

        if key not in self.memo :
            
            return -1



        self.memo.move_to_end(key)

        return self.memo[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            self.memo.move_to_end(key)

        self.memo[key]=value

        if len(self.memo)>self.cap:
            self.memo.popitem(last=False)

        
