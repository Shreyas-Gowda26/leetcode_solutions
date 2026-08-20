class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculateTotalHours(piles, speed):
            totalH = 0

            for bananas in piles:
                totalH += math.ceil(bananas / speed)

            return totalH

        maxPile = max(piles)

        low = 1
        high = maxPile
        ans = maxPile

        while low <= high:
            mid = (low + high) // 2

            totalH = calculateTotalHours(piles, mid)

            if totalH <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans