from collections import deque
from Edge import Edge

INF = 10**9

class FlowNetwork:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, capacity, cost):
        forward = Edge(v, capacity, cost)
        backward = Edge(u, 0, -cost)
        forward.rev = backward
        backward.rev = forward
        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def min_cost_max_flow(self, source, sink):
        flow = 0
        cost = 0

        while True:
            dist = [INF] * self.n
            parent = [None] * self.n
            in_queue = [False] * self.n

            dist[source] = 0
            queue = deque([source])
            in_queue[source] = True

            # SPFA — поиск кратчайшего увеличивающего пути
            while queue:
                u = queue.popleft()
                in_queue[u] = False

                for e in self.graph[u]:
                    if e.capacity > 0 and dist[e.to] > dist[u] + e.cost:
                        dist[e.to] = dist[u] + e.cost
                        parent[e.to] = (u, e)

                        if not in_queue[e.to]:
                            queue.append(e.to)
                            in_queue[e.to] = True

            if dist[sink] == INF:
                break

            # Минимальный остаточный поток
            add_flow = INF
            v = sink
            while v != source:
                u, e = parent[v]
                add_flow = min(add_flow, e.capacity)
                v = u

            # Проталкиваем поток
            v = sink
            while v != source:
                u, e = parent[v]
                e.capacity -= add_flow
                e.rev.capacity += add_flow
                cost += e.cost * add_flow
                v = u

            flow += add_flow

        return flow, cost