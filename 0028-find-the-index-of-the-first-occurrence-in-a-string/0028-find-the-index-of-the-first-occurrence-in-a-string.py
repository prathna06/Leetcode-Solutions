class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        counter=0

        if needle in haystack:
            print(haystack.split())
            return haystack.index(needle)
        else:
             return -1
                


        
