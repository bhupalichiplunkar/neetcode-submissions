class Node:
    def __init__(self, value=None, next_node=None):
        self.val = value
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr: 
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # index out of bound 

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.next)
        self.head.next = new_node
        if self.tail == self.head:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        prev = self.head
        i = 0
        while prev and i < index:
            prev = prev.next
            i += 1
        if not prev or not prev.next:
            return False
        if prev.next == self.tail:
            self.tail = prev
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        curr = self.head.next
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr