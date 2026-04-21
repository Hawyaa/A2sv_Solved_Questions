class Solution(object):
    def removeInvalidParentheses(self, s):
        self.result = []
        self.visited = set()
        
        left_remove = 0
        right_remove = 0
        
        for char in s:
            if char == '(':
                left_remove += 1
            elif char == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1
        
        self.dfs(s, 0, 0, left_remove, right_remove, "")
        return self.result
    
    def dfs(self, s, index, balance, left_remove, right_remove, current):
        if index == len(s):
            if balance == 0 and left_remove == 0 and right_remove == 0:
                self.result.append(current)
            return
        
        key = (index, balance, left_remove, right_remove, current[-10:] if current else "")
        if key in self.visited:
            return
        self.visited.add(key)
        
        char = s[index]
        
        if char == '(' and left_remove > 0:
            self.dfs(s, index + 1, balance, left_remove - 1, right_remove, current)
        elif char == ')' and right_remove > 0:
            self.dfs(s, index + 1, balance, left_remove, right_remove - 1, current)
        
        if char == '(':
            self.dfs(s, index + 1, balance + 1, left_remove, right_remove, current + '(')
        elif char == ')':
            if balance > 0:
                self.dfs(s, index + 1, balance - 1, left_remove, right_remove, current + ')')
        else:
            self.dfs(s, index + 1, balance, left_remove, right_remove, current + char)