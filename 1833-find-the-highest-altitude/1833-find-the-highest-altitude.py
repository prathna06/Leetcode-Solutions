class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr=0
        ans=[0]
        for i in gain:
            curr += i
            ans.append(curr)
        return max(ans)