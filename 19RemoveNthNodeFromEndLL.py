# Remove N-th node from the end of a Linked List
# Problem Statement: Given a linked list, and a number N. Find the Nth node from the end of this linked list and delete it. Return the head of the new modified linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
#   <<<<<<<<<<__________________________________________     coded this part as logical part     ______________________________________________>>>>>>>>>>>
        dummy = ListNode()
        dummy.next = head
        fp, sp = dummy, dummy
        for i in range(n):
            fp = fp.next
        while fp.next != None:
            sp = sp.next
            fp = fp.next
        sp.next = sp.next.next
        return dummy.next


#   <<<<<<<<<<__________________________________________     till here     ______________________________________________>>>>>>>>>>>





def createLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for item in lst[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to print a linked list.
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    n = 2
    
    solution = Solution()
    head = createLinkedList(input_list)

    print("Original Linked List:")
    printLinkedList(head)

    new_head = solution.removeNthFromEnd(head, n)
    
    print("\nLinked List after removal:")
    printLinkedList(new_head)