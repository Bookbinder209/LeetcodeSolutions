class Solution(object):
    def hasCycle(self, head):

        if head is None:
            return False
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next
            if fast == slow:
                return True
            
            slow = slow.next
            fast = fast.next

            if fast == slow:
                return True

        return False
            
            

            
            