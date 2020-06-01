from collections import defaultdict
from math import inf
content= open("0083_matrix.txt", 'r')
c = content.readlines()
content.close()
A=[list(map(int,i[:-1].split(','))) for i in c]
lmt=len(A)-1

graph=defaultdict(dict)
graph[0]={(0,0):A[0][0]}
def neigh(x,y):
    global graph
    if x>0:
        graph[(x,y)][(x-1,y)]=A[x-1][y]
    if x<lmt:
        graph[(x,y)][(x+1,y)]=A[x+1][y]
    if y<lmt:
        graph[(x,y)][(x,y+1)]=A[x][y+1]
    if y>0:
        graph[(x,y)][(x,y-1)]=A[x][y-1]

for i in range(80):
    for j in range(80):
        neigh(i,j)

def dijkstra(gr,start,end):
    # Requirements
    distance=defaultdict(lambda:inf)
    distance[start]=0
    parent={}
    not_checked=gr

    # Main loop

    while not_checked:
        actual_node=None

        for i in not_checked:
            if actual_node==None:
                actual_node=i
            elif distance[actual_node]>distance[i]:
                actual_node=i
        for x,y in not_checked[actual_node]:
            neighbor=(x,y)
            weight=not_checked[actual_node][neighbor]
            if weight+distance[actual_node]<distance[neighbor]:
                distance[neighbor]=weight+distance[actual_node]
                parent[neighbor]=actual_node
        not_checked.pop(actual_node)

    if distance[end]==inf:
        print("No path")

    else:
        cur=end
        path=[]
        while cur!=start:
            path.append(cur)
            cur=parent[cur]
        path.append(start)
        print(f"Distance: {distance[end]}")
        return

dijkstra(graph,0,(79,79))
