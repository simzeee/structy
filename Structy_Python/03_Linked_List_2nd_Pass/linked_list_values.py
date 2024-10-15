# def linked_list_values(head):
#   current = head

#   result = []

#   while current is not None:
#     result.append(current.val)
#     current = current.next

#   return result

def linked_list_values(head):
  values = []
  fill_values(head, values)

  return values

def fill_values(head, values):
  if head is None:
    return 
  values.append(head.val)
  fill_values(head.next, values)