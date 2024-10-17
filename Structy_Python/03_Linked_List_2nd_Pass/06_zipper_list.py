def zipper_lists(head_1, head_2):
    current_1 = head_1.next
    current_2 = head_2
    tail = head_1
    counter = 0

    while current_1 is not None and current_2 is not None:
        print(current_1.val, current_2.val)
        if counter % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        counter = counter + 1

    if current_1 is None:
        tail.next = current_2
    else:
        tail.next = current_1

    return head_1
