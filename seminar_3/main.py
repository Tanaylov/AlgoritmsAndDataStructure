class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def app(self, value):
        end = Node(value)
        n = self
        while n.next:
            n = n.next
        n.next = end
    def revLL(head, tail = None):
        while head:
            head.next, tail, head = tail, head, head.next
        return tail
    def printLL(head):
        while head:
            print(head.data, end=' -> ' if head.next else '')
            head = head.next
        print()

ll = Node(1)
ll.app(2)
ll.app(3)
ll.app(5)
ll.printLL()
#node = ll
# print(node.data)
# while node.next:
#     node = node.next
#     print(node.data)
ll1 = ll.revLL()
ll1.printLL()