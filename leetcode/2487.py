class Solution(object):
    def removeNodes(self, head):
        stack = []
        cur = head
        
        while cur:
            while stack and cur.val > stack[-1].val:
                stack.pop()
            stack.append(cur)
            cur = cur.next
        
        dummy = ListNode()
        cur = dummy
        for node in stack:
            cur.next = node
            cur = cur.next
        cur.next = None
        
        return dummy.next