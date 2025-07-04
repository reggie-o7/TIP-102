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
kk_slider.next = harriet
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