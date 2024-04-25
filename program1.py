class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        stack = []
        parentheses_map = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in parentheses_map.values():
                stack.append(char)
            elif char in parentheses_map.keys():
                if not stack or stack[-1] != parentheses_map[char]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack if stack else True

        pass
    



  

