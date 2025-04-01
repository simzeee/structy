
# def sum_list(head):
#   sum = 0
#   current = head

#   while current is not None:
#     sum += current.val
#     current = current.next

#   return sum

def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)