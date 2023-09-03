# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
#   <<<<<<<<<<__________________________________________     coded this part as logical part     ______________________________________________>>>>>>>>>>>
        dummy = ListNode()
        firstNode = dummy
        carry = 0
        while l1 or l2 or carry:
            temp=0
            if l1:
                temp+=l1.val
                l1 = l1.next
            if l2:
                temp+=l2.val
                l2 = l2.next
            temp+=carry
            carry = temp//10
            node = ListNode(temp%10)
            firstNode.next = node
            firstNode = firstNode.next
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
    # Create two linked lists representing numbers (e.g., 243 and 465).
    l1 = createLinkedList([2, 4, 3])
    l2 = createLinkedList([5, 6, 4])
    
    # Create a Solution object and add the two numbers.
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    
    # Print the original linked lists and the result.
    print("Number 1:")
    printLinkedList(l1)
    
    print("\nNumber 2:")
    printLinkedList(l2)
    
    print("\nSum:")
    printLinkedList(result)