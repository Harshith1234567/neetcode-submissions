class TimeMap:

    def __init__(self):
        self.dic={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.dic:
            self.dic[timestamp] = {key:value}
        else:
            self.dic[timestamp][key]=[value]
        print(self.dic)
            
        

    def get(self, key: str, timestamp: int) -> str:
        for i in range(timestamp,-1,-1):
            print(timestamp,i)
            if i in self.dic and key in self.dic[i].keys():
                return self.dic[i][key]

        return ""
        
