
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

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head
    temp = head
    n = 1
    while temp.next:
        n+=1
        temp = temp.next
    temp.next = head
    k = k % n
    brk = n - k
    while brk:
        temp = temp.next
        brk -=1
    head = temp.next
    temp.next = None
    return head





# utility function to print list
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)
    return




if __name__ == '__main__':
    head = None
    # inserting Node
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)


    print("Original list: ", end='')
    printList(head)


    k = 2
    # calling function for rotating right of the nodes by k times
    newHead = rotateRight(head, k)


    print("After", k, "iterations: ", end='')
    printList(newHead)  # list after rotating nodes