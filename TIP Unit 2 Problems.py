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


def main():
    # Breakout Problems Session 1
    # Standard Problem Set Version 1
    # P1
    assert (total_treasure(treasure_map1)) == 15

    # P2
    assert (can_trust_message(message2)) == False
        
    print("All Test cases passed!")
if __name__ == "__main__":
    main()