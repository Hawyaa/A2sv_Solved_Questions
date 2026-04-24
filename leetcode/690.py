class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # Create a map for quick lookup
        emp_map = {}
        for emp in employees:
            emp_map[emp.id] = emp
        
        # DFS using stack
        total = 0
        stack = [id]
        
        while stack:
            curr_id = stack.pop()
            employee = emp_map[curr_id]
            total += employee.importance
            
            # Add all subordinates to the stack
            for sub_id in employee.subordinates:
                stack.append(sub_id)
        
        return total