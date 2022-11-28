from parse_instance import parse_instance
from collections import defaultdict


def run_greed(file_name): 

    # parse the text file for sets and elements
    # runs in O(p)
    row, sets = parse_instance(file_name) 
    m, n, k, p = row[:]
    print(k)

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

    # E holds selected sets 
    E = [] 

    for size in range(max_size, 0, -1):
        if size in lengths: 
            while len(lengths[size]) != 0: 
                x = lengths[size].pop() 
                E.append(x)
                for e in sets[x]: 
                    for s in set_members[e]: 
                        if x != s: 
                            s_2 = sets[s]
                            lengths[len(s_2)].remove(s)
                            s_2.remove(e)
                            lengths[len(s_2)].add(s)
    return E

print(run_greed('instance01.txt'))