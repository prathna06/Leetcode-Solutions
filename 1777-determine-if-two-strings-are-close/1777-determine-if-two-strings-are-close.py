class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1= Counter(word1)
        c2=Counter(word2)
        n1=Counter([ word for word in c1.values()])
        n2=Counter([ word for word in c2.values()])
        print(c1,c2,n1,n2)
        return c1==c2 or (n1==n2 and set(word1)==set(word2))


        