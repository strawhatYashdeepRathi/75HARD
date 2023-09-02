class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next






class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#   <<<<<<<<<<__________________________________________     coded this part as logical part     ______________________________________________>>>>>>>>>>>
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if (l1.val > l2.val):
            l1, l2 = l2, l1
        headnode = l1

        while l1 and l2:
            test = None
            while l1 and l1.val <=l2.val:
                test = l1
                l1 = l1.next
            test.next = l2
            l1, l2 = l2, l1
        return headnode


#   <<<<<<<<<<__________________________________________     till here     ______________________________________________>>>>>>>>>>>







def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Helper function to create a linked list from a list.
def createLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for item in lst[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Example usage:
if __name__ == "__main__":
    l1 = createLinkedList([1, 2, 4])
    l2 = createLinkedList([1, 3, 5])
    
    solution = Solution()
    merged_list = solution.mergeTwoLists(l1, l2)
    
    print("Merged Linked List:")
    printLinkedList(merged_list)