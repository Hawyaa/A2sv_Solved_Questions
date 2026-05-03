class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(s, open_count, close_count):
            # Base case: if we've used all pairs
            if len(s) == 2 * n:
                result.append(s)
                return
            
            # Add an opening parenthesis if we have any left
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            
            # Add a closing parenthesis if it wouldn't exceed open_count
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result