def linked_list_iterative(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next


def linked_list_recursive(head):
    if head is None:
        return
    print(head.val)
    linked_list_recursive(head.next)
