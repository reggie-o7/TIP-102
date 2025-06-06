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
        


#################################################

def main():
    # P1
    welcome()

    # P2
    greeting("Michael")

    # P3
    assert print_catchphrase("Tigger") == "TTFN: Ta-ta for now!"

    print("All Test cases passed!")
if __name__ == "__main__":
    main()