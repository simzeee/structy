def max_path_sum(root):
  if root is None:
    return float("-inf")
  # terminated the path
  if root.left is None and root.right is None:
    # return the sum
    return root.val

  max_left = max_path_sum(root.left)
  max_right = max_path_sum(root.right)
  
  return root.val + max(max_left, max_right)