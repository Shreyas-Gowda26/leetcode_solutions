class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = int(a,2)
        b1 = int(b,2)
        su = a1+b1
        res = bin(su)
        return str(res[2:])