# Breakout Problems Session 1
# Advanced Problem Set Version 1
# Problem 1: Arrange Guest Arrival Order
def arrange_guest_arrival_order(arrival_pattern):
    res = []
    stack = []

    for i in range(len(arrival_pattern) + 1):
        stack.append(i + 1)
            
        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                res.append(stack.pop())
    return ''.join(map(str, res))

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  

# Problem 2: Reveal Attendee List in Order
def reveal_attendee_list_in_order(attendees):
  pass

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  

