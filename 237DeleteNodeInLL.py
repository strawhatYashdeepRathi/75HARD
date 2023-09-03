# delete a node given only the node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val           # copy next node to this node and direct its next to next.next 
        node.next = node.next.next



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
    # Create a linked list from a list (e.g., [4, 5, 1, 9]).
    linked_list = createLinkedList([4, 5, 1, 9])

    # Select a node to delete (e.g., node with value 5).
    node_to_delete = linked_list.next

    # Create a Solution object and delete the selected node.
    solution = Solution()
    solution.deleteNode(node_to_delete)

    # Print the updated linked list.
    print("Linked List after deleting the node:")
    printLinkedList(linked_list)