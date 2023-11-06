class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for index in range(len(s)):
            substr=[]
            while s[index]==')' and stack and stack[-1]!='(':
                substr.append(stack.pop())    
            if stack and stack[-1]=='('and s[index]==')':
                stack.pop()
            for char in substr:
                stack.append(char)
            if s[index]!= ')':
                stack.append(s[index])
        return ''.join(stack) 
