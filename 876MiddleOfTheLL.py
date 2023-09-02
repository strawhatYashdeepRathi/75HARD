# 876. Middle of the Linked List
# Easy
# 10.4K
# 307
# Companies
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


class Node:
  def __init__(self) -> None:
    self.data = None
    self.next = None

# reverse a Linked List

def middle(head):
    #                first get the length of list divide by 2 and iterate again to get the head
    # if not head:
    #   return None
    # count = 0
    # test = head
    # while test.next:
    #   count+=1
    #   test = test.next
    # n = count +1
    # mid = (n)//2  # no matter what this will work like if we have length of 6 mid = 3 by 3 iteration we will get 4th element, if len 5 mid = 2 we will get 3rd element in 2 iterations which is all we need
    # for i in range(mid):
    #   head = head.next
    # return head

    #                  tortoise and rabbit approach

    fp = head
    sp = head
    while fp and fp.next:
      sp = sp.next
      fp = fp.next.next
    return sp


def push(pointer, new_data):
  newNode = Node()
  newNode.data = new_data
  newNode.next = pointer
  pointer = newNode
  return pointer

def printlist(node):
  while node !=None:
    print(node.data, end=" ")
    node = node.next
  print("\n")

if __name__ == '__main__':

  head = None
  head = push(head, 6)
  head = push(head, 5)
  head = push(head, 4)
  head = push(head, 3)
  head = push(head, 2)

  print("The linked list is this:", end=" ")
  printlist(head)
  head = middle(head)
  print("Reversed linked list:", end=" ")
  printlist(head)


