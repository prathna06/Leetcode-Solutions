class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        newArr=[0]
        newArr=[0]
        highestAlt=0 
        for i in range(len(gain)):
            highestAlt = highestAlt +gain[i]
            newArr.append(highestAlt)      
        return max(newArr)

