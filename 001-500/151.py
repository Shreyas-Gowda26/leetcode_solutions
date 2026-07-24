class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        i = len(s)-1
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            if i < 0:
                break
            
            j = i

            while i >= 0 and s[i]!=" ":
                i-=1

            ans.append(s[i+1:j+1])

        return " ".join(ans)
    
    #Using Built In's

    class Solution:
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)
