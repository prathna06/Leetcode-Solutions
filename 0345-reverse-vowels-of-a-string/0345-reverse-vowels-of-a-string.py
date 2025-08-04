class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = deque()
        char_list = list(s)

# Modify the character at the specified index
        

# Join the list back into a string

        for i in s:
            if i.lower() in ['a','e','i','o','u']:
                stack.append(i)
        for i in range(len(s)):
            if s[i].lower() in ['a','e','i','o','u']:
                char_list[i] = stack.pop()
                
        return "".join(char_list)



