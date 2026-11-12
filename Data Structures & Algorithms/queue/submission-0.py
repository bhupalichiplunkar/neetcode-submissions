class Node: 
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        old_node = self.tail.prev
        old_node.next = new_node
        new_node.prev = old_node
        new_node.next = self.tail
        self.tail.prev = new_node
        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        old_node = self.head.next
        new_node.next = old_node
        old_node.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty(): 
            return -1
        target = self.tail.prev
        new_tail = target.prev
        new_tail.next = self.tail
        self.tail.prev = new_tail
        return target.val
        

    def popleft(self) -> int:
        if self.isEmpty(): 
            return -1
        target = self.head.next
        new_head = target.next
        new_head.prev = self.head
        self.head.next = new_head
        return target.val
