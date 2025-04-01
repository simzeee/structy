def linked_list_find(head, target):
    current = head
    while current is not None:
        if current.val == target:
            return True
        else:
            current = current.next
    return False


# Recursive


def linked_list_find_recursive(head, target):
    if head is None:
        return False
    if head.val == target:
        print("true")
        return True
    return linked_list_find(head.next, target)
