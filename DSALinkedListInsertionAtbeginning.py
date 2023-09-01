# Insert an element at beginning of the singly linked list

class Node:
  def __init__(self) -> None:
    self.data = None
    self.next = None



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
