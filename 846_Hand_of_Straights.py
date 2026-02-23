class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize!=0:
            return False 

        handCount = Counter(hand)
        hand.sort()

        for num in hand:
            if handCount[num]: 
                for i in range(num,num+groupSize):
                    if handCount[i] == 0: 
                        return False
                    handCount[i]-=1

        return True  


        # time O(nLogN + N*G)
        # space O(n)