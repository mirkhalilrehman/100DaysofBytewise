# 8. Reverse Linked List
#    - Write a program to reverse a singly-linked list.
#    - Expected output: If the input linked list is `1 -> 2 -> 3 -> 4 -> 5`, the output should be `5 -> 4 -> 3 -> 2 -> 1`.


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    print(" -> ".join(map(str, values)))

linked_list = create_linked_list([1, 2, 3, 4, 5])
reversed_list = reverse_linked_list(linked_list)
print_linked_list(reversed_list)
