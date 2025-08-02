# Problem 1: Counting the Layers of a Sandwich
def count_layers(sandwich):
    if not sandwich or len(sandwich) == 1:
        return 1
    return 1 + count_layers(sandwich[1])

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))


# Problem 2: Reversing Deli Orders
def recursive_order(lst):
    if not lst:
        return []

    return [lst[-1]] + recursive_order(lst[:-1])

def reverse_orders(orders):
    orders = orders.strip().split(' ')
    print(orders)
    return ' '.join(recursive_order(orders))

print(reverse_orders("Bagel Sandwich Coffee"))


# Problem 3: Sharing the Coffee
def can_split_coffee(coffee, n):
    if not coffee:
        return False
    if sum(coffee) % n == 0:
        return True
    return can_split_coffee(coffee[1:],n)


def can_split_coffee(coffee, n):
    total = sum(coffee)
    
    # If total isn't divisible evenly, we can't split it
    if total % n != 0:
        return False
    
    target = total // n
    used = [False] * len(coffee)
    
    def backtrack(i, k, subset_sum):
        # If we’ve formed k groups successfully
        if k == 0:
            return True
        # If current group hits the target, form next group
        if subset_sum == target:
            return backtrack(0, k - 1, 0)
        
        for j in range(i, len(coffee)):
            if not used[j] and subset_sum + coffee[j] <= target:
                used[j] = True
                if backtrack(j + 1, k, subset_sum + coffee[j]):
                    return True
                used[j] = False  # backtrack
        
        return False
    
    return backtrack(0, n, 0)

# print(can_split_coffee([4, 4, 8], 2))
# print(can_split_coffee([5, 10, 15], 4))


# Problem 4: Super Sandwich
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a

    nexta = sandwich_a.next
    nextb = sandwich_b.next

    sandwich_a.next = sandwich_b

    sandwich_b.next = merge_orders(nexta, nextb)

    return sandwich_a


sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

# print_linked_list(merge_orders(sandwich_a, sandwich_b))
# print_linked_list(merge_orders(sandwich_a, sandwich_c))


# Problem 5: Super Sandwich II
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    # If either list is empty, return the other
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a

    # Start with the first node of sandwich_a
    head = sandwich_a
    
    # Loop through both lists until one is exhausted
    while sandwich_a and sandwich_b:
        # Store the next pointers
        next_a = sandwich_a.next
        next_b = sandwich_b.next
        
        # Merge sandwich_b after sandwich_a
        sandwich_a.next = sandwich_b
        
        # If there's more in sandwich_a, add it after sandwich_b
        if sandwich_a:
            sandwich_b.next = next_a
        
        # Move to the next nodes
        sandwich_a = next_a
        sandwich_b = next_b

    # Return the head of the new merged list
    return head


# Problem 6: Ternary Expression
def evaluate_ternary_expression_iterative(expression):
    stack = []
    
    # Traverse the expression from right to left
    for i in range(len(expression) - 1, -1, -1):
        char = expression[i]
        
        if stack and stack[-1] == '?':
            stack.pop()  # Remove the '?'
            true_expr = stack.pop()  # True expression
            stack.pop()  # Remove the ':'
            false_expr = stack.pop()  # False expression
            
            if char == 'T':
                stack.append(true_expr)
            else:
                stack.append(false_expr)
        else:
            stack.append(char)
    
    return stack[0]

def evaluate_ternary_expression_recursive(expression):
    pass


# print(evaluate_ternary_expression_recursive("T?2:3"))
# print(evaluate_ternary_expression_recursive("F?1:T?4:5"))
# print(evaluate_ternary_expression_recursive("T?T?F:5:3"))
