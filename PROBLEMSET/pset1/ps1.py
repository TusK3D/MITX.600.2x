###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict

class Items(object):
    """a class to maintain the cows name and weights.
    """
    def __init__(self, n, w):
        self.name = n
        self.weight = w
    
    def getName(self):
        return self.name
    def getWeight(self):
        return self.weight
    
    def __str__(self) -> str:
        return self.name + " : " + str(self.weight)
    
def build_items(_names, _weights):
    """assumes names and weights are lists
    names - Str, weights - int"""
    L = []
    for i in range(len(_names)):
        L.append(Items(_names[i], _weights[i]))
    return L
    
# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_names = []
    cow_weights = []
    for key, value in cows.items():
        cow_names.append(key)
        cow_weights.append(value)
    mCows = build_items(cow_names, cow_weights)
    mCows = sorted(mCows, key = lambda x:x.getWeight(), reverse = True)
    taken = [0 for i in range(len(mCows))]
    result = []
    
    while 0 in taken:
        total_cows, total_weights = [], 0
        for i in range(len(mCows)):
            if taken[i] == 0:
                if mCows[i].weight <= (limit - total_weights):
                    total_cows.append(mCows[i].getName())
                    taken[i] = 1
                    total_weights += mCows[i].getWeight()
        if len(total_cows) == 0:
            return result
        result.append(total_cows,)
    return result

            
                






# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_names = []
    cow_weights = []
    for key, value in cows.items():
        cow_names.append(key)
        cow_weights.append(value)
    mCows = build_items(cow_names, cow_weights)
    result = []
    max = 0
    for partition in get_partitions(mCows):
        total_weight = 0
        total_cows = []
        for item in partition:
                temp = []
                temp_weight = 0
                for n in item:
                    temp_weight += n.getWeight()
                    temp.append(n.getName())
                # if temp_weight > limit:
                    # break
                total_cows.append(temp,)
                if temp_weight > total_weight:
                    total_weight = temp_weight
            
        if total_weight <= limit:
            if max < total_weight:
                    max = total_weight
                    result = total_cows
        
    return result

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("PROBLEMSET/pset1/ps1_cow_data.txt")
limit= 10
print(cows)

start = time.time()
## code to be timed
print(greedy_cow_transport(cows, limit))
end = time.time()
print(end - start)

print("BOOYEAH")

start = time.time()
print(brute_force_cow_transport(cows, limit))
## code to be timed
end = time.time()
print(end - start)
