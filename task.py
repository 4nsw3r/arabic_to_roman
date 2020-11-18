class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        digit={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }   
        for i in range(len(s)-1): 

            if (digit[s[i]]<digit[s[i+1]]):

                res=res-digit[s[i]]
            elif (digit[s[i]]>=digit[s[i+1]]):
                res=res+digit[s[i]]
        res=res+digit[s[len(s)-1]]
        return res


