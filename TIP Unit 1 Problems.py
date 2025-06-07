# Problem 1: Hundred Acre Wood
def welcome():
	print("Welcome to The Hundred Acre Wood!")
     
# Problem 2: Greeting
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin")

# Problem 3: Catchphrase
def print_catchphrase(character):
    characters = {"Pooh":"Oh bother!","Tigger":"TTFN: Ta-ta for now!","Eeyore":"Thanks for noticing me.","Christopher Robin":"Silly old bear."}
    for key,value in characters.items():
        if key == character:
            return value
    return f"Sorry! I don't know {character}'s catchphrase!"
        
# Problem 4: Return Item
def get_item(items, x):
    if 0 <= x < len(items):
        return items[x]
    else:
        return None
    
# Problem 5: Total Honey
def sum_honey(hunny_jars):
    sum = 0
    for i in hunny_jars:
        sum += i
    return sum


#################################################

def main():
    # P1
    welcome()

    # P2
    greeting("Michael")

    # P3
    assert print_catchphrase("Tigger") == "TTFN: Ta-ta for now!"

    # P4
    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 2
    assert (get_item(items, x)) == 'roo'

    # P5
    hunny_jars = [2, 3, 4, 5]
    assert sum_honey(hunny_jars) == 14

    print("All Test cases passed!")
if __name__ == "__main__":
    main()