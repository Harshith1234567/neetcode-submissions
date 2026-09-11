class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        com=[]
        for i in range(len(speed)):
            com.append([position[i],speed[i], ((target-position[i] )/ speed[i])])

        com = sorted(com, key=lambda com:com[0],reverse = True)
        print(com)

        start=0
        count=1
        for i in range(1,len(com)):
            if com[start][2] >= com[i][2]:
                continue
            start=i
            count+=1 


        return count


        