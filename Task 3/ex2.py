# 2. Palindrome Linked List
#    - Write a program to determine if a given linked list is a palindrome.
#    - Expected output: If the linked list is `1 -> 2 -> 3 -> 2 -> 1`, the output should be "The linked list is a palindrome." If the linked list is `1 -> 2 -> 3 -> 4 -> 5`, the output should be "The linked list is not a palindrome."

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_palindrome(head):
    vals = []
    current = head
    while current:
        vals.append(current.value)
        current = current.next
    return vals == vals[::-1]

def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

linked_list = create_linked_list([1, 2, 3, 2, 1])
result = "The linked list is a palindrome." if is_palindrome(linked_list) else "The linked list is not a palindrome."
print(result)
