def iterative_depth_first_leaf_list(root):
    if root is None:
        return []

    leaves = []
    stack = [root]
    while stack:
        current = stack.pop()
        if current.left is None and current.right is None:
            leaves.append(current.val)

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return leaves

def recursive_leaf_list(root):
  leaves = []
  _leaf_list(root, leaves)
  return leaves

def _leaf_list(root, leaves):
  if root is None:
    return 
    
  if root.left is None and root.right is None:
    leaves.append(root.val)
    
  _leaf_list(root.left, leaves)
  _leaf_list(root.right, leaves)