class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=['a','e','i','o','u','A','E','I','U','O']
        i=0
        j=len(s)-1
        s=list(s)
        while(i<j):
            if s[i]  not in arr:
                i+=1
            elif  s[j] not in arr:
                j-=1
            else:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1

        return ''.join(s)
        