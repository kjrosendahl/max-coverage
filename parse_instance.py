import csv 
from collections import defaultdict

def parse_instance(file_name): 
    sets = defaultdict(set)
    with open(file_name, newline='') as csvfile: 
        reader = csv.reader(csvfile, delimiter = ' ')
        params = next(reader)
        # m, n, k, p = params[:]
        for row in reader: 
            s, elmnt = row[:]
            sets[s].add(elmnt)
        return(params, sets)
        

