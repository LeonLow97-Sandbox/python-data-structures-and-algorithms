# Create Node
class Node:
    def __init__(self, val=None):
        self.val = val # Assign initial value
        self.next = None # Initialize ref as  null (reference)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # to print out the singly linked list
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def push(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self

    # remove a node from the end of the Linked List
    def pop(self):
        if self.head is None:
            return None
        # looping through the Linked List to find the second last tail
        current = self.head
        newTail = current
        while (current.next):
            newTail = current
            current = current.next
        
        self.tail = newTail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return current
    
    # removing a node from the beginning of the Linked List
    def shift(self):
        if self.head is None:
            return None
        currentHead = self.head
        self.head = currentHead.next
        self.length -= 1
        if (self.length == 0):
            self.tail = None

        return currentHead
    
    # adding a new node to the beginning of the Linked List
    def unshift(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self


SLL = SinglyLinkedList()
node1 = Node(1)
node2 = Node(2)

SLL.head = node1
node1.next = node2
SLL.tail = node2

SLL.push(3)
SLL.push(4)
print(SLL.shift().val)
SLL.unshift(10)

print([node.val for node in SLL])

