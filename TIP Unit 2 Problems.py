# Breakout Problems Session 1
# Advanced Problem Set Version 1
# Problem 1: Counting Treasure
def total_treasure(treasure_map):
    total = 0
    for key, value in treasure_map.items():
        total += value
    return total

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

# Problem 2: Pirate Message Check
def can_trust_message(message):
    message = "".join(message.split())
    if len(message) < 26:
        return False
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        if alphabet[i] not in message:
            return False
    return True  

def can_trust_message_sets(message):
    message = set(message.replace(' ',''))
    return set("abcdefghijklmnopqrstuvwxyz").issubset(message)

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

# Problem 3: Find All Duplicate Treasure Chests in an Array
def find_duplicate_chests(chests):
    ans = []
    dict = {}
    for i in range(len(chests)):
        if chests[i] in dict:
            dict[chests[i]] += 1
        else:
            dict[chests[i]] = 1
    for key, value in dict.items():
        if value == 2:
            ans.append(key)
    return ans

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

def find_duplicate_chests_opt(chests):
    ans = []
    for num in chests:
        index = abs(num) - 1
        if chests[index] < 0:
            ans.append(abs(num))
        else:
            chests[index] *= -1
    return ans

# Problem 4: Booby Trap
def is_balanced(code):
    code = [*code]
    print(code)
    dict = {}
    for i in range(len(code)):
        if code[i] in dict:
            dict[code[i]] += 1
        else:
            dict[code[i]] = 1
    for key, value in dict.items():
        check 





code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
# print(is_balanced(code2)) 




def main():
    # Breakout Problems Session 1
    # Standard Problem Set Version 1
    # P1
    assert (total_treasure(treasure_map1)) == 15

    # P2
    assert (can_trust_message(message2)) == False

    # P3
    assert (find_duplicate_chests(chests1)) == [3,2]

    # P4
    # assert (is_balanced(code1)) == True
        
    print("All Test cases passed!")
if __name__ == "__main__":
    main()