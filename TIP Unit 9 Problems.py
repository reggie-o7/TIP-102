from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root


class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    if not order1 and not order2:
        return None
    if not order1:
        return order2
    if not order2:
        return order1
    
    new = TreeNode(order1.val + order2.val)

    new.left = merge_orders(order1.left, order2.left)
    new.right = merge_orders(order1.right, order2.right)

    return new

# """
#      1             2         
#     /  \         /   \       
#    3    2       1     3   
#  /               \      \   
# 5                 4      7   
# """
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))

# P2
from collections import deque

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if not design:
        return []
    
    ans = []
    queue = deque([design])

    while queue:
        node = queue.popleft()
        ans.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return ans

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
# print(print_design(croquembouche))

#P3

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    if not cake:
        return 0
    
    queue = deque([cake])
    ans = 0
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
        ans += 1
    return ans

# def max_tiers(cake):
#     if not cake:
#         return 0
#     return 1 + max(max_tiers(cake.left), max_tiers(cake.right))

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))

#P4

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    pass


"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

# print(max_tiers(cake))


#P5
class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def can_fulfill_order(inventory, order_size):
    if not inventory:
        return False
    if not inventory.left and not inventory.right:
        return inventory.val == order_size
    
    remainder = order_size-inventory.val
    return can_fulfill_order(inventory.left, remainder) or can_fulfill_order(inventory.right, remainder)



"""
             5
           /   \
          4     8
        /      /  \
       11     13   4
      /  \          \
     7   2           1   
"""

# Using build_tree() function included at top of the page
quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

# print(can_fulfill_order(baked_goods, 22))
# print(can_fulfill_order(baked_goods, 2))
