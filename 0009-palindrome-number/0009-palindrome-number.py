class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        print(s[::-1])
        if s != s[::-1]:   
            return False
        else:
          return  True

                
        