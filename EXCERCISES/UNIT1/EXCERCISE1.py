import random
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'
    
def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]

def buildRandomItems(n, maxVal, maxCost):
    return [Item(str(i),10*random.randint(1,maxVal),random.randint(1,maxCost))
            for i in range(n)]


# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 0:
                bag1.append(items[j])
            if (i // 3**j) % 3 == 1:
                bag2.append(items[j])
        yield bag1,bag2

L = buildItems()
L = buildRandomItems(10, 90, 250)
#for i in range(15): L.append(i) 
t = powerSet(L)
lp = list(t)
for item in lp:
    print(item)
