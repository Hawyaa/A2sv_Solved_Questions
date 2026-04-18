class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        
        for ch in s:
            if ch == '(':
                stack.append(0)  # marker for new depth
            else:  # ch == ')'
                if stack[-1] == 0:
                    # Found "()"
                    stack.pop()
                    stack.append(1)
                else:
                    # Found "(A)" where A is a sum on top
                    score = 0
                    while stack and stack[-1] != 0:
                        score += stack.pop()
                    stack.pop()  # remove the 0 marker
                    stack.append(2 * score)
        
        return sum(stack)