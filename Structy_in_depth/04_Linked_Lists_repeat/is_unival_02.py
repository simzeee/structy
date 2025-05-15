def is_univalue_list(head, target_val=None):
    if head is None:
        return True
    if target_val is None or head.val == target_val:
        target_val = head.val
        return is_univalue_list(head.next, target_val)
    else:
        return False
