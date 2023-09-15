class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highestAlt=0 
        maxVal=0
        for i in range(len(gain)):
            highestAlt = highestAlt +gain[i]
            maxVal = max(maxVal,highestAlt)    
        return maxVal

