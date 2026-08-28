class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        rsum = 0
        maxSum = 0
        for i in range (0,k):
            lsum = lsum + cardPoints[i]
            maxSum = lsum

            rindex = len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum = lsum - cardPoints[i]
            rsum = rsum + cardPoints[rindex]
            rindex -=1
            maxSum = max(maxSum,lsum+rsum)

        return maxSum