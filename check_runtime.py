from greedy_max import run_greedy
from pathlib import Path
import random
from collections import defaultdict
import time 
import matplotlib.pyplot as plt

def make_file(params, lst): 

    f_path = Path(r"C:\Users\kjros\Documents\GitHub\max-coverage\sample")
    with open(f_path, 'w') as f: 
        f.write(' '.join(map(str, params)))
        for x in lst:
            f.write('\n')
            f.write(' '.join(map(str, x)))

def random_instance(): 

    max_n = 2000
    max_m = 100

    m = random.randint(1,max_m)
    n = random.randint(1,max_n)
    k = random.randint(1, m)
    p = random.randint(m,m*n)

    print(m,n,k,p)

    params = [m,n,k,p]
    lst = []

    d = defaultdict(set)
    for s in range(1,m+1): 
        nums = [x for x in range(1,n+1)]
        random.shuffle(nums)
        d[s] = nums
   

    count = 0
    for s in range(1,m+1): 
        elmnt = d[s].pop() 
        lst.append([s,elmnt])
        count += 1
    while count < p: 
        s = random.randint(1,m+1)
        if len(d[s]) != 0: 
            elmnt = d[s].pop(0)
            lst.append([s,elmnt])
            count += 1

    make_file(params, lst)

    t = time.time() 
    run_greedy('sample')
    passed = time.time() - t
    return(sum(params), passed) 

x_data = []
y_data = [] 
for i in range(50): 
    print(i)
    x, y = random_instance() 
    x_data.append(x)
    y_data.append(y)

plt.plot(x_data,y_data, 'ro')
plt.show()
