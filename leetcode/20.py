class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:  # Closing bracket
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:  # Opening bracket
                stack.append(char)
        
        return not stack