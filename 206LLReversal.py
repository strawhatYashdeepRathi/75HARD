# Reverse a Linked List
# Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.

# Examples:

# Input Format: 
# head = [3,6,8,10]
# This means the given linked list is 3->6->8->10 with head pointer at node 3.

# Result:
# Output = [10,6,8,3]
# This means, after reversal, the list should be 10->6->8->3 with the head pointer at node 10.


class Node:
  def __init__(self) -> None:
    self.data = None
    self.next = None

# reverse a Linked List

def reversell(head):
    #   {********        Iterative method          ********}
    # prev, curr = None, head
    # while curr:
    #     temp = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr = temp
    # printlist(prev)
    # return prev
    if not head:
      return None
    tempHead = head
    if head.next:
      tempHead = reversell(head.next)
      head.next.next = head
    head.next = None
    return tempHead


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
  head = reversell(head)
  print("Reversed linked list:", end=" ")
  printlist(head)
