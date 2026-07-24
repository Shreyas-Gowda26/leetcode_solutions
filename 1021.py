class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        deposit = 0
        for ch in s:
            if ch == "(":
                if deposit>0:
                    ans.append(ch)
                deposit+=1
            else:
                deposit-=1
                if deposit>0:
                    ans.append(ch)
            
        return "".join(ans)