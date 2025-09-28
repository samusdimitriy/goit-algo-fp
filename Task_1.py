class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __str__(self):
        if not self.head:
            return "Empty list"
        result = []
        current = self.head
        while current:
            result.append(f"({current.data})")
            current = current.next
        return " --> ".join(result)

    def display(self):
        print(self)

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        self.head = prev

    def sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            sorted_head = self.insert_into_sorted(sorted_head, current)
            current = next_node

        self.head = sorted_head

    @staticmethod
    def insert_into_sorted(sorted_head, node):
        if sorted_head is None or node.data <= sorted_head.data:
            node.next = sorted_head
            return node

        current = sorted_head

        while current.next is not None and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node

        return sorted_head

    def merge(self, other):
        dummy = Node()
        tail = dummy
        p1, p2 = self.head, other.head

        while p1 and p2:
            if p1.data <= p2.data:
                tail.next = Node(p1.data)
                p1 = p1.next
            else:
                tail.next = Node(p2.data)
                p2 = p2.next
            tail = tail.next

        while p1:
            tail.next = Node(p1.data)
            tail = tail.next
            p1 = p1.next

        while p2:
            tail.next = Node(p2.data)
            tail = tail.next
            p2 = p2.next

        result = LinkedList()
        result.head = dummy.next
        return result


def main():
    llist = LinkedList()
    for data in [11, 99, 7, 12, 34, 9, 1, 101]:
        llist.append(data)

    print("Original list:")
    llist.display()

    llist.reverse()
    print("\nReversed list:")
    llist.display()

    llist.sort()
    print("\nSorted list:")
    llist.display()

    llist2 = LinkedList()
    for data in [17, 999, 2, 68, 99, 79, 33]:
        llist2.append(data)
    llist2.sort()

    merged_list = llist.merge(llist2)
    print("\nMerged sorted lists:")
    merged_list.display()


if __name__ == "__main__":
    main()
