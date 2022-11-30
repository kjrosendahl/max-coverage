from parse_instance import parse_instance
from collections import defaultdict
import csv

def run_greedy(file_name): 

    # Parse the text file for sets and elements
    # runs in O(p)
    params, sets = parse_instance(file_name) 
    m, k = int(params[0]), int(params[2])

    # Holds size of largest set to start
    # runs in O(m)
    max_size = max(len(sets[s]) for s in sets.keys())

    # dictionaries used to keep track of: 
    # which elements belong in which sets 
    # number of uncovered elements in each set
    # allow for faster variant of greedy algorithm 
    set_members = defaultdict(list)
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
    # runs in O(p)
    for size in range(max_size, 0, -1):
        if lengths.get(size):
            while len(lengths[size]) != 0: 
                # return if already selected a maximum of k sets 
                if len(Q) == k: 
                    return Q
                # select a set X that covers most amount of uncovered elements
                X = lengths[size].pop() 
                Q.append(X)
                # for each new element that X covered, consider all other unselected sets s_2 that has the new element
                for elmnt in sets[X]: 
                    for s_2 in set_members[elmnt]: 
                        if X != s_2: 
                            els = sets[s_2]
                            lengths[len(els)].remove(s_2)
                            # remove now covered element from s_2 
                            els.remove(elmnt)
                            # decrease the number of uncovered elements that s_2 contains
                            lengths[len(els)].add(s_2)
    
    # if we have found sets that cover all elements but don't have min(m,k) sets, then randomly add extra sets 
    # runs in O(m)
    set_indices = set(s for s in sets.keys()) 
    sets_left = set_indices.difference(set(Q))
    while len(Q) < min(m,k): 
        Q.append(sets_left.pop()) 

    return Q

## ---------------------------------- ## 

def run_instances(num_files): 

    for i in range(1,num_files+1): 
        if i < 10: 
            file_number = str(0) + str(i)
        else: 
            file_number = str(i)

        # initialize input and output files 
        input_file_name = 'instance' + file_number 
        output_file_name = 'solution' + file_number
        
        # run greedy algorithm 
        Q = run_greedy(input_file_name)

        # write to solution file
        with open(output_file_name, 'w') as csvfile: 
            writer = csv.writer(csvfile, delimiter = ' ')
            writer.writerow(Q)

## ---------------------------------- ## 

if __name__ == "__main__": 
    run_instances(1)