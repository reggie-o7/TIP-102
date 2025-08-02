# Problem 1: Building a Playlist
# class SongNode:
# 	def __init__(self, song, next=None):
# 		self.song = song
# 		self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
#     print()
		
        
# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

# node1 = SongNode("Bad Romance")
# node2 = SongNode("Party Rock Anthem", node1)
# node3 = SongNode("Uptown Funk", node2)

# top_hits_2010s = node3

# print_linked_list(top_hits_2010s)


# Problem 2: Top Artists
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    ans = {}
    
    curr = playlist
    while curr:
        if curr.artist in ans:
            ans[curr.artist] += 1
        else:
            ans[curr.artist] = 1
        curr = curr.next
    return ans


playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))


# Problem 3: Glitching Out
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next and current.next.next:
        if current.next.song == song:
            current.next = current.next.next
            return playlist_head
        else:
            current = current.next

    return playlist_head 

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))


# Problem 4: On Repeat
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):

    slow = playlist_head
    fast = playlist_head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False
    
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

# print(on_repeat(song1))


# Problem 5: Looped
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
    
    slow = playlist_head
    fast = playlist_head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        ans = 0

        if slow == fast:
            ans = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                ans += 1
            return ans

    return ans


song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

# print(loop_length(song1))


# Problem 6: Volume Control
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def count_critical_points(song_audio):
    if not song_audio or not song_audio.next or not song_audio.next.next:
        return 0
    
    prev = song_audio
    curr = song_audio.next
    next = curr.next
    counter = 0

    while next:
        if (curr.value > prev.value and curr.value > next.value) or (curr.value < prev.value and curr.value < next.value):
            counter += 1
        prev = prev.next
        curr = curr.next
        next = next.next

    return counter


song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))





class Node:
	def __init__(self, house, score, next=None):
            self.house = house
            self.value = score
            self.next = next


# For testing
def print_linked_list(head):
    current = head
    while current:
        print((current.house, current.value), end=" -> " if current.next else "\n")
        current = current.next

def count_element(house_points, score):
	
    counter=0
    curr = house_points
    while curr:
        if curr.value == score:
            counter += 1
        curr = curr.next
    return counter

house_points = Node("Gryffindor", 600, 
                Node("Ravenclaw", 300,
                    Node("Slytherin", 500,
                        Node("Hufflepuff", 600))))

score = house_points.value

print(count_element(house_points, score))