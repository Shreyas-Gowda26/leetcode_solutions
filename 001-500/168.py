class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        a = [chr(x) for x in range(ord("A") ,ord("Z")+2)]
        res = ""
        while columnNumber>0:
            columnNumber-=1
            res += a[columnNumber%26]
            columnNumber//=26
        return res[::-1]
