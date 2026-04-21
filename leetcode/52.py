class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        # columns[i] = True if column i is occupied
        columns = [False] * n
        # diag1[i] = True if diagonal (row+col) is occupied
        diag1 = [False] * (2 * n - 1)
        # diag2[i] = True if diagonal (row-col+n-1) is occupied
        diag2 = [False] * (2 * n - 1)
        
        def backtrack(row):
            if row == n:
                self.count += 1
                return
            
            for col in range(n):
                if columns[col] or diag1[row + col] or diag2[row - col + n - 1]:
                    continue
                
                # Place queen
                columns[col] = True
                diag1[row + col] = True
                diag2[row - col + n - 1] = True
                
                # Recurse to next row
                backtrack(row + 1)
                
                # Remove queen (backtrack)
                columns[col] = False
                diag1[row + col] = False
                diag2[row - col + n - 1] = False
        
        backtrack(0)
        return self.count