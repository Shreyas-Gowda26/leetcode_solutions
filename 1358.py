class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            freq = {'a':0, 'b':0, 'c':0}

            for j in range(i,n):
                freq[s[j]]+=1

                if freq['a']>0 and freq['b']>0 and freq['c']>0:
                    count+=1

        return count