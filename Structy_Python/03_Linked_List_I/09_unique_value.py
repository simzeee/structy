def is_univalue_list(head):
    test_value = head.val
    current = head

    while current is not None:
        if current.val != test_value:
            return False
        current = current.next
    return True
