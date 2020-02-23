from itertools import permutations as p
print(str([x for x in p(range(10))][10**6-1]).replace(", ","").replace("(","").replace(")",""))