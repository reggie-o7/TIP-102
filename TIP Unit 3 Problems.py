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
# # print(post_compare("a#c", "b")) 

# Breakout Problems Session 2
# Standard Problem Set Version 1
# Problem 1: Manage Performance Stage Changes
def manage_stage_changes(changes):
    stack_schedule = []
    stack_cancel = []

    for i in changes:
        if "Schedule" in i:
            stack_schedule.append(i[-1])
        elif i == 'Cancel':
            if stack_schedule:
                canceled = stack_schedule.pop()
                stack_cancel.append(canceled)
        else:
            if i == "Reschedule":
                if stack_cancel:
                    reschedule = stack_cancel.pop()
                    stack_schedule.append(reschedule)
    return stack_schedule

# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]))

# Problem 2: Queue of Performance Requests
from collections import deque
def process_performance_requests(requests):
    queue = deque()

    while len(requests) > 0:

        max_val = 0
        for i in requests:
            if i[0] > max_val:
                max_val = i[0]
    
        for j in requests:
            if j[0] == max_val:
                queue.append(j[1])
                requests.remove(j)
                break

    return list(queue)
    

# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

# Problem 3: Collecting Points at Festival Booths
def collect_festival_points(points):
    stack = []

    for i in points:
        stack.append(i)

    ans = 0
    while stack:
        ans += stack.pop()
    return ans

# print(collect_festival_points([5, 8, 3, 10])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8])) 

# Problem 4: Festival Booth Navigation
def booth_navigation(clues):
    stack = []

    for i in clues:
        if i == "back":
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return stack

# clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues)) 

# clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues)) 

# clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues))

# Problem 5: Merge Performance Schedules
def merge_schedules(schedule1, schedule2):
    ans = ''

    largest = max(len(schedule1), len(schedule2))

    for i in range(largest):
        if len(schedule1) > i:
            ans += schedule1[i]
        if len(schedule2) > i:
            ans += schedule2[i]
    return ans

# print(merge_schedules("abc", "pqr")) 
# print(merge_schedules("ab", "pqrs")) 
# print(merge_schedules("abcd", "pq"))

# Problem 6: Next Greater Event
def next_greater_event(schedule1, schedule2):
    stack = []

    for i in schedule1:
        for j in range(len(schedule2)):
            if schedule2[j] == i:
                index = j
                if len(schedule2) > index+1 and schedule2[index+1] > schedule2[index]:
                    stack.append(schedule2[index+1])
                    break
                else:
                    stack.append(-1)
                    break
    return stack
    
# print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
# print(next_greater_event([2, 4], [1, 2, 3, 4]))
# print(next_greater_event([3], [5, 3, 6])) 

# Problem 7: Sort Performances by Type
def sort_performances_by_type(performances):
    stack = []

    evens = []
    for i in performances:
        if i % 2 == 0:
            evens.append(i)

    while evens:
        max_val = (max(evens))
        stack.append(max_val)
        evens.remove(max_val)

    odds = []
    for j in performances:
        if j % 2 != 0:
            odds.append(j)

    while odds:
        min_val = (min(odds))
        stack.append(min_val)
        odds.remove(min_val)

    return stack

print(sort_performances_by_type([3, 1, 2, 4]))
print(sort_performances_by_type([0]))
