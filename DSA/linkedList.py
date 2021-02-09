class Node:
    def __init__(self):
        self.data = None
        self.next: Node
        self.next = None


def traverse(head_node: Node):
    ptr = head_node
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.next


def insertHead(head_node: Node, data):
    ptr = Node()
    ptr.data = data
    ptr.next = head_node
    return ptr


def insertAtIndex(head_node: Node, data, index: int):
    ptr = Node()
    p = head_node
    i = 0
    while i != index - 1:
        p = p.next
        i += 1
    ptr.data = data
    ptr.next = p.next
    p.next = ptr
    return ptr


def insertAfterNode(prevNode: Node, data):
    ptr = Node()
    ptr.next = prevNode.next
    prevNode.next = ptr
    ptr.data = data
    return ptr


def insertAtEnd(head_node: Node, data):
    ptr = Node()
    p = head_node
    while p is not None:
        p = p.next
    p.next = ptr
    ptr.next = None
    ptr.data = data
    return ptr


def deleteHead(head_node: Node):
    ptr = head_node
    head_node = head_node.next
    del ptr
    return head_node


def deleteAtIndex(head_node: Node, index):
    if index == 0:
        return deleteHead(head_node)
    p = head_node
    q = p.next
    for i in range(index - 1):
        p = p.next
        q = q.next
    p.next = q.next
    del q
    return head_node


def deleteTail(head_node: Node):
    p = head_node
    q = head_node.next
    while q.next is not None:
        p = p.next
        q = q.next
    p.next = None
    del q
    return head_node


def deleteAtValue(head_node: Node, value):
    p = head_node
    q = head_node.next
    while q.data != value and q.next is not None:
        p = p.next
        q = q.next
    if q.data == value:
        p.next = q.next
        del q

    else:
        print("Value not in the linked list")
    return head_node


def len(head_node: Node):
    i = 0
    p = head_node
    while p is not None:
        p = p.next
        i += 1
    return i


if __name__ == "__main__":
    head = Node()
    first = Node()
    second = Node()
    tail = Node()

    head.data = 5
    head.next = first

    first.data = 6
    first.next = second

    second.data = 7
    second.next = tail

    tail.data = 8
    tail.next = None

    head = deleteHead(head)
    traverse(head)
    print(len(head))
