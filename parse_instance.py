import csv 

def parse_instance(file_name): 
    set_members = dict() 
    with open(file_name, newline='') as csvfile: 
        reader = csv.reader(csvfile, delimiter = ' ')
        row1 = next(reader)
        # m, n, k, p = row1[:]
        for row in reader: 
            s, elmnt = row[:]
            if s in set_members.keys(): 
                set_members[s].add(elmnt)
            else: 
                set_members[s] = set(elmnt)
        return(row1, set_members)

