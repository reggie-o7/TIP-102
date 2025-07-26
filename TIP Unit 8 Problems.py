# Problem 1: Grafting Apples
from collections import deque 
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")

root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")

root.right.right = TreeNode("Gala")
root.right.left = TreeNode("Crab")

# Using print_tree() included at the top of this page
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

# print_tree(root)


# Problem 2: Calculating Yield
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if not root:
        return None
    

    left = root.left.val
    right = root.right.val

    if root.val == '+':
        return left + right
    elif root.val == "-":
        return left - right
    elif root.val == "*":
        return left * right
    elif root.val == "/":
        return left / right
    else:
        return None

"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))

# Problem 3: Ivy Cutting
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    ans = []
    curr = root
    while curr:
        ans.append(curr.val)
        curr = curr.right
    return ans

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))


# Problem 4: Ivy Cutting II
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    if not root:
        return []
    return [root.val] + right_vine(root.right)
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))


# Problem 5: Count the Tree Leaves
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)
    

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# print(count_leaves(oak1))
# print(count_leaves(oak2))


# Problem 6: Pruning Plans
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    if not root:
        return []
    return survey_tree(root.left) + survey_tree(root.right) + [root.val]

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# print(survey_tree(magnolia))


# Problem 7: Foraging Berries
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def harvest_berries(root, threshold):
    if not root:
        return 0
    
    ans = 0
    if root.val > threshold:
        ans += root.val

    ans += harvest_berries(root.left, threshold)
    ans += harvest_berries(root.right, threshold)

    return ans

"""
       4
     /   \
   10     6
  /  \     \
 5    8    20
"""
bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

# print(harvest_berries(bush, 6))
# print(harvest_berries(bush, 30))

# Problem 8: Flower Fields
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_flower(root, flower):
    if not root:
        return False
    
    if root.val == flower:
        return True
    
    return find_flower(root.left, flower) or find_flower(root.right, flower)

"""
         Rose
        /    \
       /      \
     Lily     Daisy
    /    \        \
Orchid  Lilac    Dahlia
"""

flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))
print(find_flower(flower_field, "Hibiscus"))

