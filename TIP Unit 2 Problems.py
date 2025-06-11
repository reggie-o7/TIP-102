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




def main():
    # Breakout Problems Session 1
    # Standard Problem Set Version 1
    # P1
    assert (total_treasures(treasure_map1)) == 15
        
    print("All Test cases passed!")
if __name__ == "__main__":
    main()