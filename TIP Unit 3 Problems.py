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

# print(arrange_guest_arrival_order("IIIDIDDD"))  
# print(arrange_guest_arrival_order("DDD"))  

# Problem 2: Reveal Attendee List in Order
from collections import deque 
def reveal_attendee_list_in_order(attendees):
    queue = deque()

    descend = sorted(attendees)
    descend.reverse()

    for i in descend:
        if queue:
            queue.appendleft(queue.pop())
        queue.appendleft(i)
    return list(queue)


# print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
# print(reveal_attendee_list_in_order([1,1000]))  
     
# Standard Problem Set Version 1
# Problem 1: Post Format Validator
def is_valid_post_format(posts):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for i in posts:
        if i in bracket_map.values():
            stack.append(i)
        elif i in bracket_map:
            if not stack or stack[-1] != bracket_map[i]:
                return False
            stack.pop()
    return True

# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))
  
# Problem 2: Reverse User Comments Queue
def reverse_comments_queue(comments):
    stack = []

    while len(comments) > 0:
        stack.append(comments.pop(0))
    rev_com = []
    while len(stack) > 0:
        rev_com.append(stack.pop())
    return rev_com

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# Problem 3: Check Symmetry in Post Titles
def is_symmetrical_title(title):
    title1 = title.replace(' ', '').lower()

    clean_title = ''
    for i in title1:
        code = ord(i)
        if (97 <= code <= 122):
             clean_title += i

    left = 0
    right = len(clean_title) - 1

    while left < right:
        if clean_title[left] == clean_title[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 

# Problem 4: Engagement Boost
def engagement_boost(engagements):
    result = [0] * len(engagements)
    left = 0
    right = len(engagements) - 1
    position = len(engagements) - 1 

    while left <= right:
        if (engagements[left] ** 2) > (engagements[right] ** 2):
            result[position] = engagements[left] ** 2
            left += 1
        else:
            result[position] = engagements[right] ** 2
            right -= 1
        position -= 1
    return result

# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))

# Problem 5: Content Cleaner
def clean_post(post):
    stack = []

    for i in post:
        if len(stack) > 0 and abs(ord(stack[-1]) - ord(i)) == 32:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)

# print(clean_post("poOost")) 
# print(clean_post("abBAcC")) 
# print(clean_post("s"))

# Problem 6: Post Editor
from collections import deque 
def edit_post(post):
    queue = deque()

    res = []
    for i in range(len(post)):
        if post[i] != ' ':
            queue.appendleft(post[i])
        else:
            while queue:
                res.append(queue.popleft())
            res.append(post[i])
    while queue:
        res.append(queue.popleft())
                
    return ''.join(res)

# print(edit_post("Boost your engagement with these tips")) 
# print(edit_post("Check out my latest vlog"))

# Problem 7: Post Compare
def remove_hash(text)->str:
    stack = []
    for i in range(len(text)):
        if text[i] == '#':
            if stack:
                stack.pop()
        else:
            stack.append(text[i])
    return ''.join(stack) 

def post_compare(draft1, draft2):
    return remove_hash(draft1) == remove_hash(draft2)

# print(post_compare("ab#c", "ad#c"))
# print(post_compare("ab##", "c#d#")) 
# print(post_compare("a#c", "b")) 