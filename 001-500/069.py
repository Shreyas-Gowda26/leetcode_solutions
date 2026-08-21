#Time Complexity - O(n)
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        for i in range(x+1):
            if i*i <= x:
                ans = i
            else:
                break
        return ans

#Using Binary Search
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        low = 1
        high = x
        while low<=high:
            mid = (low +high)//2
            if mid * mid <= x:
                ans = mid
                low = mid+1
            else:
                high = mid - 1
            
        return ans