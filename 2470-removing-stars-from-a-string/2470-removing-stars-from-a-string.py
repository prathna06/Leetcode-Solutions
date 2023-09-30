class Solution:
    def removeStars(self, s: str) -> str:
        stack =[]
        str1=""
        for i in s:
            if i =="*":
                stack.pop()
            else:
                stack.append(i)
        
        return str1.join(stack)

               
        