from parse_instance import parse_instance
from collections import defaultdict
import csv

def run_greedy(file_name): 

    # parse the text file for sets and elements
    # runs in O(p)
    row, sets = parse_instance(file_name) 
    k = row[2]
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
    # TODO: verify this works in O(p) time 
    # runs by removing one element at a time from sets 
    # bounded by (sum(|s|) for s in F) = O(p)
    # see exercise 35.3-3 in textbook 
    # TODO: ask prof if we are allowed to return less than min(m, k) if we found a solution which covers all elements (no unecessary sets)
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
                            # decrease the number of available elements that s_2 could cover 
                            lengths[len(s_2)].add(s)
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
    run_instances(3)