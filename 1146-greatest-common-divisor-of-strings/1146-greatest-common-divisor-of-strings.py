class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        minStr = str1 if len(str1) < len(str2) else str2
        for i in range(len(minStr)+1, 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                if self.isDivisible(minStr[:i], str1) and self.isDivisible(minStr[:i], str2):
                    return minStr[:i]
        return ""


    def isDivisible(self, shortString, longString):
        print(shortString, longString)
        j = 0
        shortStringLen = len(shortString)
        while j < len(longString)-1:
            if (longString[j:j+shortStringLen] == shortString):
                j += len(shortString)
            else:
                return False
        return True


