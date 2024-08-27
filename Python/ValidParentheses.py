class Solution(object):
    def isValid(self, s):
        if len(s) %2 == 1:
            return False

        stack = []
    
        for c in s:
            stack.append(c)
            if stack[-1] in (')', '}', ']'):
                num = stack.pop()
                if len(stack) < 1: 
                    return False
                
                if num == ')':
                    if stack[-1] != '(':
                        return False

                if num == '}':
                    if stack[-1] != '{':
                        return False

                if num == ']':
                    if stack[-1] != '[':
                        return False
                stack.pop()
            
        return len(stack) == 0