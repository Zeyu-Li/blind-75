class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if len(stack) == 0: return False
                popped = stack.pop()
                if mapping[popped] != char: return False
                
          
        return not len(stack)