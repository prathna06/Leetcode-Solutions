class Solution:
    def reverseVowels(self, s: str) -> str:
        list1=list(s)
        pos=[]
        val=[]
        vowels=["a","e","i","o","u"]
        for i in range(len(list1)):
            if list1[i].lower() in vowels:
                val.append(list1[i])
                pos.append(i)
        val=val[::-1]
        for i in range(len(pos)):
            list1[pos[i]]=val[i]
        return ''.join(list1)

                

                
        