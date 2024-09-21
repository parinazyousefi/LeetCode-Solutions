# piles = [3,6,7,11], h = 8

# input= list of piles + h=>the time we have
# output=speed of eating banas===>k
# operations:
# k could be:[1,2,3,4,5,6,7,8,9,10,11]
# l                      h
# worst case =11 ==>it is not slow  enough
# if it is 11 :ceil(3/11)+(6/11)+(7/11)+11/11==4 hours it takes to finish the bananas which is less than the time we have


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high

        while low <= high:
            k = (high + low) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                result = min(k, result)
                high = k - 1
            else:
                low = k + 1
        return result
