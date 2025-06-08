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

# Problem 1: Hunny Hunt
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Breakout Problems Session 2
# Standard Problem Set Version 1
# Problem 1: Reverse Sentence
def reverse_sentence(sentence):
    sentence = sentence.strip().split()
    return ' '.join(sentence[::-1])

# Problem 2: Goldilocks Number
def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    max_val = max(nums)
    min_val = min(nums)

    for i in nums:
        if i != max_val and i != min_val:
            return i
    return -1

# Problem 3: Delete Minimum
def delete_minimum_elements(hunny_jar_sizes):
    new_list = []
    while len(hunny_jar_sizes) > 0:
        min_val = min(hunny_jar_sizes)
        new_list.append(min_val)
        hunny_jar_sizes.remove(min_val)
    return new_list

# Problem 4: Sum of Digits
def sum_of_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_of_digits(num // 10)

# Problem 5: Bouncy, Flouncy, Trouncy, Pouncy
def final_value_after_operations(operations):
    trigger = 1
    for i in operations:
        if i == 'bouncy' or i == 'flouncy':
            trigger += 1
        else:
            trigger -= 1
    return trigger

# Problem 6: Acronym
def is_acronym(words, s):
    if len(s) != len(words):
        return False 
    for i in range(len(s)):
        if words[i][0] != s[i]:
            return False
    return True

# Problem 7: Good Things Come in Threes
def make_divisible_by_3(nums):
    count = 0
    for i in nums:
        if i % 3 != 0:
            count += 1
    return count

# Problem 8: Exclusive Elements
def exclusive_elemts(lst1, lst2):
    ans = []
    for i in lst1:
        if i not in lst2:
            ans.append(i)
    for i in lst2:
        if i not in lst1:
            ans.append(i)
    return ans





#################################################

def main():
    # Breakout Problems Session 1
    # Standard Problem Set Version 1
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

    

    # Breakout Problems Session 2
    # Standard Problem Set Version 1
    # P1
    sentence = "tubby little cubby all stuffed with fluff"
    assert (reverse_sentence(sentence)) == 'fluff with stuffed all cubby little tubby'

    # P2
    assert goldilocks_approved([1, 2]) == -1

    # P3
    hunny_jar_sizes = [5, 3, 2, 4, 1]
    assert (delete_minimum_elements(hunny_jar_sizes)) == [1, 2, 3, 4, 5]

    # P4
    num = 423
    assert (sum_of_digits(num)) == 9

    # P5
    assert final_value_after_operations(["trouncy", "flouncy", "flouncy"]) == 2

    # P6  
    words = ["christopher", "robin", "milne"]
    s = "crm"
    assert (is_acronym(words, s)) == True
    
    # P7
    nums = [3, 6, 9]
    assert (make_divisible_by_3(nums)) == 0

    # P8
    lst1 = ["pooh", "roo"]
    lst2 = ["piglet", "eeyore", "owl", "kanga"]
    assert (exclusive_elemts(lst1, lst2)) == ["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]

        
    print("All Test cases passed!")
if __name__ == "__main__":
    main()