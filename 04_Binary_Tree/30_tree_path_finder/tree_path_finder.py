# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def path_finder_slow(root, target):
#   if root is None:
#     return None
  
#   if root.val == target:
#     return [root.val]
  
#   left_path = path_finder_slow(root.left, target)
  
#   right_path = path_finder_slow(root.right, target)
  
#   if left_path is not None:
#     return [ root.val, *left_path]
  
#   if right_path is not None:
#     return [ root.val, *right_path]

def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  else:
    return result[::-1]

def _path_finder(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [root.val]
  
  left_path = path_finder_slow(root.left, target)
  right_path = path_finder_slow(root.right, target)

  if left_path is not None:
    left_path.append(root.val)
    return left_path

  if right_path is not None:
    right_path.append(root.val)
    return right_path