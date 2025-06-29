
def welcome():
	print("Welcome to The Hundred Acre Wood!")
	
welcome()

# Problem 3: Catchphrase
def print_catchphrase(character):
	characters = {"Pooh":"Oh bother!","Tigger":	"TTFN: Ta-ta for now!","Eeyore":"Thanks for noticing me.","Christopher Robin":"Silly old bear."}
	if character in characters:
		print(characters[character])
	else:
		print(f"Sorry! I don't know {character}'s catchphrase!")

print(print_catchphrase('Pooh'))
print(print_catchphrase('Piglet'))









