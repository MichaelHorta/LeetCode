class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        fromStartingEnded = False
        fromEndEnded = False
        zeroCountInMiddle = 0
        zeroCountInMiddle = 0
        zeroCountFromStart=0
        zeroCountFromEnd=0
        count=0
        countA=0
        countB=0
        for i in range(len(flowerbed)):

            if flowerbed[i] == 0 and fromStartingEnded == True:
                zeroCountInMiddle+=1

            if flowerbed[i] == 0 and fromStartingEnded == False:
                zeroCountFromStart+=1

            if flowerbed[len(flowerbed)-i-1] == 0 and fromEndEnded == False:
                zeroCountFromEnd+=1

            if flowerbed[i] == 1 and fromStartingEnded == False:
                fromStartingEnded = True
                countA+=(int)(zeroCountFromStart/2)

            if flowerbed[len(flowerbed)-i-1] == 1 and fromEndEnded == False:
                fromEndEnded = True
                countB+=(int)(zeroCountFromEnd/2)

            if flowerbed[i] == 1 and fromStartingEnded == True:
                if zeroCountInMiddle > 0:
                    count = count + (int)((zeroCountInMiddle-1)/2)
                    zeroCountInMiddle=0

        if zeroCountFromStart == zeroCountFromEnd and countA == 0 and countB == 0:
            if zeroCountFromStart > 1:
                count+=(int)((zeroCountFromStart+1)/2)
            if len(flowerbed) == 1 and flowerbed[0] == 0:
                return True
        if count + countA + countB >= n:
            return True
        return False
