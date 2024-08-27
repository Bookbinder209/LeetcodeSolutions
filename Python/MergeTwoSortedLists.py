class Solution(object):
    def mergeTwoLists(self, list1, list2):
        header = ListNode()
        tail = header
       

        while list1 and list2:
            if list1.val <= list2.val:
               tail.next= list1
               list1= list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1 is not None:
            tail.next = list1
        elif list2 is not None:
            tail.next = list2

        return header.next
            
        