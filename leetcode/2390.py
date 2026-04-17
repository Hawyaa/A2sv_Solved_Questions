class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(len(s)):
            if s[i]!="*":
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)
        