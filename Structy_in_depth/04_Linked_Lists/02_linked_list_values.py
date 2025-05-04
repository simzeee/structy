def linked_list_values(head):
    if head is None:
        return []

    values = _linked_list_values(head, [])
    return values


def _linked_list_values(head, values_list):
    if head is None:
        return
    values_list.append(head.val)
    _linked_list_values(head.next, values_list)
    return values_list
