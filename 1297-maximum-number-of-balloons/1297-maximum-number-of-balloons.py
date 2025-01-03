class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp={'b':0,'a':0,'l':0,'o':0,'n':0}
        for txt in text:
            if txt in mp:
                mp[txt]+=1
        return min(mp['b'],mp['a'],mp['l']//2,mp['o']//2,mp['n'])
        

        
        

        