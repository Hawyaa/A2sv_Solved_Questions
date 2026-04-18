class Solution(object):
    def decodeString(self, s):
        stack = []
        
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # Get the substring to repeat
                substring = []
                while stack and stack[-1] != '[':
                    substring.append(stack.pop())
                substring = ''.join(reversed(substring))
                
                # Pop the '['
                stack.pop()
                
                # Get the number k
                k_str = []
                while stack and stack[-1].isdigit():
                    k_str.append(stack.pop())
                k = int(''.join(reversed(k_str)))
                
                # Repeat and push back
                stack.append(substring * k)
        
        return ''.join(stack)