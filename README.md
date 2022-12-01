# CS430: Team Project
### Team Members: Kaylee Rosendahl, Charles Sainegh, Ibrahim Marou
*Due: 12/2/22*

#### File Breakdown: 
- **parse_instance.py** - helper function used by the greedy algorithm to read instance files. 
- **greedy_max.py** - runs the greedy algorithm on specified number of instances. Reads each instance file and writes the solution to another file. 
- **pseudo_runtime.txt** - pseudocode for *parse_instance.py* and the greedy algorithm. Includes explanation and comments on our implemementation. Includes runtime analysis. 
- **counter_ex** - holds instance for an example where the greedy algorithm does not find an optimal solution. 

To run the algorithm, execute *greedy_max.py* with each instance file in the directory. It will write the solution files in the same location. There is no need to specify the number of instances -- as long as the first instance is "instance01" and the file names don't skip numbers, it will run on all of them. 

***

### Counter-example
We have included an instance file where the greedy algorithm does not find the optimal solution. *greedy_max.py* also writes the solution file for this instance. 

Our sets are as followed: 
S1 = {1, 2, 3, 4, 5, 6} 
S2 = {5, 6, 8, 9} 
S3 = {1, 4, 7, 10} 
S4 = {2, 5, 7, 8, 11} 
S5 = {3, 6, 9, 12} 
S6 = {10, 11} 
We let *k* = 3. The greedy algorithm will return Q = {S1, S4, S5}, covering all elements but 10. There is a better solution, S = {S3, S4, S5}, which covers all elements. 