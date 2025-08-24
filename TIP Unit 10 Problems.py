# Problem 1: Graphing Flights


"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
# No starter code is provided for this problem
# Add your code here
flights = {
    "JFK": ["LAX", "DFW"],
    "LAX": ["JFK"],
    "DFW": ["ATL", "JFK"],
    "ATL": ["DFW"]
}


# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])

# Problem 2: There and Back
def bidirectional_flights(flights):
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))

# Problem 3: Finding Direct Flights
def get_direct_flights(flights, source):
    ans = []

    for j in range(len(flights[source])):
            if flights[source][j] == 1:
                ans.append(j)
    
    return ans



flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

# print(get_direct_flights(flights, 2))
# print(get_direct_flights(flights, 3))


# # Problem 4: Converting Flight Representations
def get_adj_dict(flights):
    adj_dict = {}
    
    for i in range(len(flights)):  # iterate over each [a, b] pair
        a, b = flights[i]
        
        # Add b to a's list
        if a not in adj_dict:
            adj_dict[a] = []
        adj_dict[a].append(b)
        
        # Add a to b's list
        if b not in adj_dict:
            adj_dict[b] = []
        adj_dict[b].append(a)
    
    return adj_dict


#sess 2
# Problem 1: Can Rebook Flight
# 

def can_rebook(flights, source, dest):
    n = len(flights)
    visited = set()

    def dfs(city):
        if city == dest:
            return True
        visited.add(city)
        
        for next_city in range(n):
            if flights[city][next_city] == 1 and next_city not in visited:
                if dfs(next_city):
                    return True
        return False
    
    return dfs(source)


flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 


# Problem 2: Can Rebook Flight II
def can_rebook(flights, source, dest):
    pass



flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 