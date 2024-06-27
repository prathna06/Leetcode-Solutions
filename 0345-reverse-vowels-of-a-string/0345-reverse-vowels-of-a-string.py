class Solution:
    def reverseVowels(self, s: str) -> str:
        list1=list(s)
        i=0
        j=len(list1)-1
        vlist=['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        while i<j:
            if list1[i] in vlist and list1[j] in vlist:
                list1[i] ,list1[j]= list1[j], list1[i]
                i+=1
                j-=1
            elif list1[i] not in vlist:
                i+=1
            elif list1[j] not in vlist:
                j-=1


        return "".join(list1)
