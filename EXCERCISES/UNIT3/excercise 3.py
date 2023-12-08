def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not len(L):
        return float('NaN')
    
    u = sum([len(x) for x in L])/len(L)

    v = [(len(t)-u)**2 for t in L]
    return (sum(v)/len(v)) ** 0.5

def test_stdDevOfLengths(L):
    return stdDevOfLengths(L)

print(f"t1 = {test_stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])},\
      t2 = {test_stdDevOfLengths(L = ['a', 'z', 'p'])},\
      t3 = {test_stdDevOfLengths(L = [])}")
