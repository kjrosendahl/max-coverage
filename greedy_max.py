from parse_instance import parse_instance
from collections import defaultdict


def run_greed(file_name): 

    # parse the text file for sets and elements
    # runs in O(p)
    row, sets = parse_instance(file_name) 
    m, n, k, p = row[:]
    k = int(k)

    # holds cardinality of largest set to start
    # runs in O(m)
    max_size = max(len(sets[s]) for s in sets.keys())

    # set_members holds list of sets that have a particular element (key)
    set_members = defaultdict(list)

    # lengths holds the lengths of each set 
    lengths = defaultdict(set)

    # for set_members, this runs in O(p)
    # for lengths, this runs in O(m)
    for s, elmnts in sets.items(): 
        for elmnt in elmnts: 
            set_members[elmnt].append(s)
        lengths[len(elmnts)].add(s)

    # Q holds selected sets 
    Q = [] 

    # perform greedy algorithm: iterate through decreasing size of sets
    for size in range(max_size, 0, -1):
        if size in lengths: 
            while len(lengths[size]) != 0: 
                # return if already selected a maximum of k sets 
                if len(Q) == k: 
                    return Q
                # select a set X that covers most amount of available elements
                X = lengths[size].pop() 
                Q.append(X)
                # for each new element that X covered, consider all other unselected sets s_2 that has the new element
                for e in sets[X]: 
                    for s in set_members[e]: 
                        if X != s: 
                            s_2 = sets[s]
                            # remove now covered element from s_2 
                            lengths[len(s_2)].remove(s)
                            s_2.remove(e)
                            # decrease the number of available elemenets that s_2 could cover 
                            lengths[len(s_2)].add(s)
    return Q

print(run_greed('instance02.txt'))