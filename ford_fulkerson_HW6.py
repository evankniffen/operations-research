def main_ff():
    caps = {
        ('A','B'):4, ('A','C'):6,
        ('B','C'):4, ('B','D'):4, ('B','E'):2,
        ('C','D'):6, ('C','E'):1,
        ('D','F'):2, ('E','F'):6
    }
    flow = {e:0 for e in caps}
    residual = lambda u,v: caps.get((u,v),0) - flow.get((u,v),0) + flow.get((v,u),0)
    def find_path(u,t,visited):
        if u==t: return [t]
        visited.add(u)
        for v in ['B','C','D','E','F']:
            if (u,v) in caps or (v,u) in caps:
                if v not in visited and residual(u,v)>0:
                    p = find_path(v,t,visited)
                    if p:
                        return [u]+p
        return None
    max_flow = 0
    iteration = 1
    while True:
        path = find_path('A','F',set())
        if not path: break
        deltas = []
        for u,v in zip(path,path[1:]):
            deltas.append(residual(u,v))
        delta = min(deltas)
        print(f"iter. {iteration}: augmenting flow delta = {delta} along {path}")
        max_flow += delta
        for u,v in zip(path,path[1:]):
            if (u,v) in flow:
                flow[(u,v)] += delta
            else:
                flow[(v,u)] -= delta
        iteration += 1
    print("max flow =", max_flow)
    print("final flows:")
    for e in sorted(flow):
        print(f"{e}: {flow[e]}/{caps[e]}")

if __name__=="__main__":
    main_ff()
