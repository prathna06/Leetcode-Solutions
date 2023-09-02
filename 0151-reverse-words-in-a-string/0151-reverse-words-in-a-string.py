class Solution:
    def reverseWords(self, s: str) -> str:
        list1=s.split()
        list1= list1[::-1]
        return " ".join(list1)

        