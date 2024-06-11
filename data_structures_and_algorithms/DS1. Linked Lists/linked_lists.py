class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class LinkedListV2:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = Node(value)

    def show(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next


if __name__ == "__main__":
    node_1 = Node(1)
    node_2 = Node(3)
    node_3 = Node(5)

    linked_list = LinkedList()
    linked_list.head = node_1
    linked_list.head.next = node_2
    linked_list.head.next.next = node_3

    linked_list_v2 = LinkedListV2()
    linked_list_v2.append(2)
    linked_list_v2.append(5)
    linked_list_v2.append(7)
    linked_list_v2.append(9)
    linked_list_v2.show()