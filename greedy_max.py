from parse_instance import parse_instance

row, d = parse_instance('instance01.txt') # parsing runs in O(p)
m, n, k, p = row[:]
print(m,n,k,p)
for k, v in d.items(): 
    print(k,v)
    