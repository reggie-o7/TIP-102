# Problem 1: Villager Class 
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

apollo = Villager("Apollo", "Eagle", "pah")
# print(apollo.name)
# print(apollo.species) 
# print(apollo.catchphrase)
# print(apollo.furniture)


# Problem 2: Add Furniture
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
	
    def add_item(self, item_name):
        valid_items = [
            "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"
        ]

        if item_name in valid_items:
            self.furniture.append(item_name)

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)


# Problem 3: Group by Personality
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
	
def of_personality_type(townies, personality_type):
    ans = []
    for i in townies:    
        if i.personality == personality_type:
            ans.append(i.name)
    return ans

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))


# Problem 4: Telephone
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    # ... methods from previous problems


'''
U:
    I - villager
    O - bool
    C - 
    E -
plan: 


'''	
def message_received(start_villager, target_villager):
    active = start_villager
    while active != None:
        if active == target_villager:
            return True
        else:
            active = active.neighbor
    return False


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))


# Problem 5: Linked Up
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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Add code here to link the above nodes
kk_slider.next = harriet# Problem 6: Got One!
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head is not None: 
        print(f'I caught a {head.fish_name}!')
        head = head.next
        return head
    print(f"Aw! Better luck next time!")
    return None
harriet.next = saharah
saharah.next = isabelle

# print_linked_list(kk_slider)


# Problem 6: Got One!
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head is not None: 
        print(f'I caught a {head.fish_name}!')
        head = head.next
        return head
    print(f"Aw! Better luck next time!")
    return None


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))


# Problem 7: Fishing Probability
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):
    length = 0
    freq = 0
    active = head
    while active is not None:
        if active.fish_name == fish_name:
            freq += 1
        length += 1
        active = active.next

    if length == 0:
        return 0.00
    return round(freq / length, 2)


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))


# Problem 8: Restocking the Lake
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def restock(head, new_fish):
    if head is None:
        return Node(new_fish)
    
    active = head
    while active.next is not None:
        active = active.next

    active.next = Node(new_fish)
    return head
   
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print_linked_list(restock(fish_list, "Rainbow Trout"))


# Session 2: Linked Lists
# Problem 1: Greatest Node
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

def find_max(head):
    if head is None:
        return None
    
    max_val = float('-inf')
    curr = head
    while curr is not None:
        if curr.value > max_val:
            max_val = curr.value
        curr = curr.next
    return max_val


# head1 = Node(5, Node(6, Node(7, Node(8))))

# # Linked List: 5 -> 6 -> 7 -> 8
# # print(find_max(head1))

# head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
# print(find_max(head2))


# Problem 2: Remove Tail
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_tail(head):
    if head is None:
        return None
    
    if head.next is None:
        return None 
        
    current = head
    while current.next.next is not None:
        current = current.next

    current.next = None
    return head

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

head2 = Node("Izzy", Node("Reggie", Node("Vlad")))

# Linked List: Isabelle -> Alfonso -> Cyd
# print_linked_list(remove_tail(head))

# print_linked_list(remove_tail(head2))


# Problem 3: Delete Duplicates in a Linked List
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

def delete_dupes(head):
    temp_head = Node("temp")    # Initialize a temporary head node
    temp_head.next = head   # Point the temporary head at the input list

    prev = temp_head
    curr = head
    while curr is not None:
        if curr.next is not None and curr.value == curr.next.value:
            dup = curr.value

            while curr is not None and curr.value == dup:
                curr = curr.next
            prev.next = curr
        else:
            prev = curr
            curr = curr.next
    return temp_head.next

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
# print_linked_list(delete_dupes(head))


# Problem 4: Does it Cycle?
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    if not head:
        return False
    
    slow = head  # Starts at the head
    fast = head  # Also starts at the head

    while fast != None and fast.next != None:
        slow = slow.next
        fast= fast.next.next
    
        if slow == fast:
            return True
        
    return False

peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

# print(has_cycle(peach))


# Problem 5: Remove Nth Node From End of List
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

def remove_nth_from_end(head, n):
    temp_head = Node("temp")    # Initialize a temporary head node
    temp_head.next = head   # Point the temporary head at the input list

    slow = temp_head
    fast = temp_head

    for i in range(n):
        fast = fast.next
    
    while fast.next != None:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    
    return temp_head.next
        

head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")

# print_linked_list(remove_nth_from_end(head1, 2))
# print_linked_list(remove_nth_from_end(head2, 1))
# print_linked_list(remove_nth_from_end(head3, 1))

# Problem 6: Careful Reverse 
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
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
        
def reverse_first_k(head, k):
	if not head or k <= 1:
		return head
	
	prev = None
	curr = head
	count = 0
	
	while curr and count < k:
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
		count += 1
		
	head.next = curr
    
	return prev
		
head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

# print_linked_list(reverse_first_k(head, 3))


   