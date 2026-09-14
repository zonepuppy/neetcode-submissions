# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        head = list3
        while list1 is not None or list2 is not None:
            if list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    list3.next = ListNode()
                    list3=list3.next
                    list3.val = list1.val
                    list1 = list1.next
                    
                else:
                    list3.next = ListNode()
                    list3=list3.next
                    list3.val = list2.val
                    list2=list2.next
                    
            else:
                if list1 is None:
                    list3.next = ListNode()
                    list3=list3.next
                    list3.val = list2.val
                    list2 = list2.next 
                else:
                    list3.next = ListNode()
                    list3=list3.next
                    list3.val = list1.val
                    list1=list1.next
        return head.next
       
        