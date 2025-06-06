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

# Problem 6: Double Trouble
def doubled(hunny_jars):
    list_d = []
    for i in hunny_jars:
        list_d.append(i*2)
    return list_d

# Problem 7: Poohsticks
def count_less_than(race_times, threshold):
    ans = 0
    for i in range(len(race_times)):
        if race_times[i] < threshold:
            ans += 1
    return ans

# Problem 8: Pooh's To Do's
def print_todo_list(task):
    string = "Pooh's To Dos:\n"
    for i in range(len(task)):
        string += f'{i+1}. {task[i]}\n'
    return string

# Problem 9: Pairs
def can_pair(item_quantities):
    for i in item_quantities:
        if i % 2 != 0:
            return False
    return True

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

    # P6
    hunny_jars = [1, 2, 3]
    assert doubled(hunny_jars) == [2, 4, 6]

    # P7
    assert count_less_than([1, 5, 3, 6, 2], 4) == 3

    # P8
    assert print_todo_list([]) == "Pooh's To Dos:\n"

    # P9
    assert can_pair([]) == True

    print("All Test cases passed!")
if __name__ == "__main__":
    main()