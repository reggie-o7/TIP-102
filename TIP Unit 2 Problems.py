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
    dict1 = {}
    for i in range(len(code)):
        if code[i] in dict1:
            dict1[code[i]] += 1
        else:
            dict1[code[i]] = 1
    

    for j in dict1:
        temp_dict = dict(dict1)
        temp_dict[j] -= 1

        if temp_dict[j] == 0:
            del temp_dict[j]
        
        values = list(temp_dict.values())

        if len(set(values)) == 1:
            return True
    return False

code1 = "arghh"
code2 = "haha"

# Problem 5: Overflowing With Gold
def find_treasure_indices(gold_amounts, target):
    for i in range(len(gold_amounts)):
        for j in range(i+1, len(gold_amounts)):
            if gold_amounts[i] + gold_amounts[j] == target:
                return [i,j]


# Problem 6: Organize the Pirate Crew
def organize_pirate_crew(group_sizes):
    groups = {}
    ans = []
    for i in range(len(group_sizes)):
        if group_sizes[i] not in groups:
            groups[group_sizes[i]] = []

        groups[group_sizes[i]].append(i)

        if len(groups[group_sizes[i]]) == group_sizes[i]:
            ans.append(groups[group_sizes[i]])
            groups[group_sizes[i]] = []
    return ans

def organize_pirate_crew_with_enum(group_sizes):
    groups = {}  
    ans = []     

    for pirate_id, size in enumerate(group_sizes):
        if size not in groups:
            groups[size] = []

        groups[size].append(pirate_id)

        if len(groups[size]) == size:
            ans.append(groups[size])
            groups[size] = []

    return ans


group_sizes1 = [3, 3, 3, 3, 3, 1, 3]


# Problem 7: Minimum Number of Steps to Match Treasure Maps
def min_steps_to_match_maps(map1, map2):
    map1dict = {}
    map2dict = {}
    for i in range(len(map1)):
        if map1[i] in map1dict:
            map1dict[map1[i]] += 1
        else:
            map1dict[map1[i]] = 1
        if map2[i] in map2dict:
            map2dict[map2[i]] += 1
        else:
            map2dict[map2[i]] = 1
    ans = 0
    for key, value in map2dict.items():
        count_map_1 = map1dict.get(key,0)
        if value > count_map_1:
            ans += abs(value - count_map_1)
    return ans

map1_1 = "bab"
map2_1 = "aba"


# Problem 8: Counting Pirates' Action Minutes
def counting_pirates_action_minutes(logs, k):
    log_dict = {}
    for pirate_id, minute in logs:
        if pirate_id in log_dict:
            log_dict[pirate_id].append(minute)
        else:
            log_dict[pirate_id] = [minute]
    print(log_dict)

    ans = [0] * k
    for pirate_id in log_dict:
        unique_pam = len(set(log_dict[pirate_id]))
        if 1 <= unique_pam <= k:
            ans[unique_pam - 1] += 1
    return ans

logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5

# Breakout Problems Session 2
# Avanced Problem Set Version 1
# Problem 1: Balanced Art Collection
def find_balanced_subsequence(art_pieces):
    ans = 0
    freq = {}
    for i in art_pieces:
        freq[i] = freq.get(i, 0) + 1

    for j in freq:
        if j + 1 in freq:
            ans = max(ans, freq[j] + freq[j+1])
    return ans


art_pieces1 = [1,3,2,2,5,2,3,7]

# Problem 2: Verifying Authenticity
def is_authentic_collection(art_pieces):
    freq = {}
    for i in art_pieces:
        freq[i] = freq.get(i,0) + 1

    max_key = max(freq)
    
    if len(art_pieces) != max_key+1:
        return False
    
    for i in range(1,max_key):
        if freq.get(i,0) != 1:
            return False
        
    if freq.get(max_key, 0) != 2:
        return False
    
    return True

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

# Problem 3: Gallery Wall
def organize_exhibition(collection):
    ans = []
    freq = {}
    for i in collection:
        freq[i] = freq.get(i,0) + 1

    while any(freq[j] > 0 for j in freq):
        current_ans = []
        for j in freq:
            if freq[j] > 0:
                freq[j] -= 1
                current_ans.append(j)
        ans.append(current_ans)
    return ans


collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]

# Problem 4: Gallery Subdomain Traffic
def subdomain_visits(cpdomains):
    counts = {}  # normal dictionary

  
    for i in cpdomains:
        count_str, domain = i.split()                        # e.g. "9001 modern.artmuseum.com"
        count = int(count_str)                        # convert "9001" -> 9001
        parts = domain.split('.')                        # ['modern', 'artmuseum', 'com']

        for j in range(len(parts)):                            # Build subdomains from right to left
            subdomain = '.'.join(parts[j:])                        # e.g. "artmuseum.com", then "modern.artmuseum.com"
            if subdomain in counts:
                counts[subdomain] += count
            else:
                counts[subdomain] = count

    # Build final result
    ans = []
    for i in counts:
        ans.append(str(counts[i]) + ' ' + i)
    return ans
   

cpdomains1 = ["9001 modern.artmuseum.com"]


# Problem 5: Beautiful Collection
def beauty_sum(collection):
    pass

print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))

def count_endangered_species(endangered_species, observed_species):
    freq = {}
    for i in observed_species:
        freq[i] = freq.get(i,0) + 1

    # endangered = [*endangered_species]
    endangered = set(endangered_species)
    
    ans = 0
    for j in endangered:
        if j in freq:
            ans += freq[j]
    return ans

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

print(count_endangered_species(endangered_species1, observed_species1))


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
    assert (is_balanced(code1)) == True
        
    print("All Test cases passed!")
if __name__ == "__main__":
    main()