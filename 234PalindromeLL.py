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


def findMiddle(head):
    sp, fp = head, head
    while fp.next and fp.next.next:
        sp = sp.next
        fp = fp.next.next
    return sp


def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def isPalindrome(head):
    if not head:
        return None
    mid = findMiddle(head)
    last = reverse(mid.next)
    dummy = head
    while dummy and last:
        if dummy.val != last.val:
            return False
        dummy = dummy.next
        last = last.next
    return True


if __name__ == "__main__":
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 2)
    head = insertNode(head, 1)
    print(isPalindrome(head))