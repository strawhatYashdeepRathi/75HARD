class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return None
    #      {         ----------------    Brute force O(3N) and sc of O(N)    ------------------           }
    # mapp = {}
    # temp = head
    # while temp:
    #     newNode = Node(temp.val)
    #     mapp[temp] = newNode
    #     temp = temp.next
    # test = head
    # while test:
    #     testNode = mapp[test]
    #     testNode.next = mapp.get(test.next)
    #     testNode.random = mapp.get(test.random)
    #     test = test.next
    # return mapp[head]

    # step 1  make copy nodes similar to original LL >>>>>>>>>>>>>>>>>>>>>>>.    O(3N) ~ O(N)   and sc => O(1)
    temp = head
    
    while temp:
        copyNode = Node(temp.val)
        copyNode.next = temp.next
        temp.next = copyNode
        temp = temp.next.next

    # step 2  make copy nodes random pointers 
    itr = head
    while itr:
        if itr.random:
            itr.next.random = itr.random.next
        itr = itr.next.next
    
    # step 3  seperate copy from real one
    fresh = Node(0)
    itr = head
    t = fresh
    while itr:
        t.next = itr.next
        t = t.next
        itr.next = t.next
        itr = itr.next
    return fresh.next








def printList(head: 'Node'):
    while head:
        print(f"{head.val}:", end="")
        if head.next:
            print(head.next.val, end="")
        else:
            print("NULL", end="")
        if head.random:
            print(f",{head.random.val}", end="")
        else:
            print(",NULL", end="")
        print()
        head = head.next

if __name__ == '__main__':
    head = None

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    head = node1
    head.next = node2
    head.next.next = node3
    head.next.next.next = node4

    head.random = node4
    head.next.random = node1
    head.next.next.random = None
    head.next.next.next.random = node2

    print("Original list:(current node:node pointed by next pointer, node pointed by random pointer)")
    printList(head)

    print("Copy list:(current node:node pointed by next pointer, node pointed by random pointer)")
    newHead = copyRandomList(head)
    printList(newHead)