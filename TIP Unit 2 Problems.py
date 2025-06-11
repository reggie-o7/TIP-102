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
    message = "".join(message.strip())
    if len(message) < 26:
        return False
    alphabet = ""

message1 = "sphinx of black quartz judge my vow"




def main():
    # Breakout Problems Session 1
    # Standard Problem Set Version 1
    # P1
    assert (total_treasures(treasure_map1)) == 15
        
    print("All Test cases passed!")
if __name__ == "__main__":
    main()