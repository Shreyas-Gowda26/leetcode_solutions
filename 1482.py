#Brute
class Solution:
        def is_possible(self, bloomDay, day, m, k):
            count = 0  # count of consecutive bloomed flowers
            bouquets = 0

            for bloom in bloomDay:
                if bloom <= day:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0

            return bouquets >= m

        def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
            total_flowers = m * k
            if total_flowers > len(bloomDay):
                return -1

            low = min(bloomDay)
            high = max(bloomDay)

            for day in range(low, high + 1):
                if self.is_possible(bloomDay, day, m, k):
                    return day

            return -1