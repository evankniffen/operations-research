import heapq
# shoutout heapq gang
def main_dijkstra():
    P = [17000,19000,21000,25000,30000]
    M = [3800,5000,9700,18200,30400]
    adj = {i:[] for i in range(1,7)}
    for i in range(1,6):
        for j in range(i+1,7):
            cost = P[i-1] + sum(M[k] for k in range(j-i)) # dIJKstras 
            adj[i].append((j,cost))
    dist = {i:float('inf') for i in adj}
    prev = {}
    dist[1]=0
    pq=[(0,1)]
    while pq:
        d,u = heapq.heappop(pq)
        if d>dist[u]: continue
        for v,c in adj[u]:
            nd = d+c
            if nd<dist[v]:
                dist[v]=nd
                prev[v]=u
                heapq.heappush(pq,(nd,v))
    path=[]
    node=6
    while node in prev:
        path.append(node)
        node=prev[node]
    path.append(1)
    path.reverse()
    print("shortest:", path)
    print("cost =", dist[6])

if __name__=="__main__":
    main_dijkstra()
