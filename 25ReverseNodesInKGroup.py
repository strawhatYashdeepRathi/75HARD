class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head




# utility function to find length of the linked list
def lengthOfLinkedList(head):
    count = 0
    while head:
        count+=1
        head = head.next
    return count




# utility function to reverse k nodes in the linked list
def reverseKNodes(head, k):
    if not head or not head.next: return head

    # n = 0
    # temp = head
    # while temp:
    #     n+=1
    #     temp = temp.next

    n = lengthOfLinkedList(head)
    dummy = Node(0)
    dummy.next = head
    curr, prev, nxt = None, dummy, None
    while n >= k:
        curr = prev.next
        nxt = curr.next
        for i in range(1, k):
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
            nxt = curr.next
        prev = curr
        n -= k

    return dummy.next




# utility function to print the linked list
def printLinkedList(head):
    while head.next != None:
        print(head.val, end="->")
        head = head.next
    print(head.val)




if __name__ == "__main__":
    head = None
    k = 3
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)
    head = insertNode(head, 6)
    head = insertNode(head, 7)
    head = insertNode(head, 8)


    print("Original Linked List: ", end="")
    printLinkedList(head)
    print("After Reversal of k nodes: ", end="")
    newHead = reverseKNodes(head, k)
    printLinkedList(newHead)