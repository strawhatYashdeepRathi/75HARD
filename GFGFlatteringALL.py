class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.bottom = None

def merge(l1, l2):
    temp = Node(0)
    res = temp
    while l1 and l2:
        if(l1.val <= l2.val):
            temp.bottom = l1
            temp = temp.bottom
            l1 = l1.bottom
        else:
            temp.bottom = l2
            temp = temp.bottom
            l2 = l2.bottom
    if l1: temp.bottom = l1
    else: temp.bottom = l2
    return res.bottom


def flatten(head):
    if head == None or head.next == None:
        return head
    head.next = flatten(head.next)
    ll = merge(head, head.next)
    return head


# Helper function to print the flattened linked list
def printFlattenedList(root):
    while root:
        print(root.val, end=" -> ")
        root = root.bottom
    print("None")

# Example usage:
if __name__ == '__main__':
    # Creating a sample linked list of linked lists
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(19)
    head.next.next.next = Node(28)

    head.bottom = Node(7)
    head.bottom.bottom = Node(8)
    head.bottom.bottom.bottom = Node(30)

    head.next.bottom = Node(20)

    head.next.next.bottom = Node(22)
    head.next.next.bottom.bottom = Node(50)

    # Flatten the linked list
    flattened_head = flatten(head)

    # Print the flattened linked list
    print("Flattened Linked List:")
    printFlattenedList(flattened_head)