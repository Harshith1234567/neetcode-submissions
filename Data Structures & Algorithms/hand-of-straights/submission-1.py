class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            # print('======')
            # print(count)
            if count[num]<=0:
                continue
            t=num
            while t in count and count[t]>0:
                t-=1
            
            t+=1

            for a in range(t,t+groupSize):
                if count[a]<=0:
                    return False
                else:
                    count[a]-=1

            # print(count)

        return True
        