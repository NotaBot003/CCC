from queue import PriorityQueue

def top_sort(graph, in_degree):
    q = PriorityQueue()
    top_order = []
    for i in range(1, len(graph)):
        if in_degree[i] == 0:
            q.put(i)
    while not q.empty():
        nodes = q.get()
        top_order.append(nodes)
        for a in graph[nodes]:
            # if in_degree[a] > 0:
            in_degree[a] -= 1
            # top_order.append(nodes)
            if in_degree[a] == 0:
                q.put(a)
    return top_order

node = 7
graph = [[] for i in range(node + 1)]
in_degree = [0 for i in range(node + 1)]
edges = [(1, 7), (1, 4), (2, 1), (3, 4), (3, 5)]

a = int(input())
b = int(input())
while a > 0 and b > 0:
    edges.append((a, b))
    a = int(input())
    b = int(input())

for a, b in edges:
    # a, b = a - 1, b - 1
    graph[a].append(b)
    in_degree[b] += 1

order = top_sort(graph, in_degree)
# for i in range(len(order)):


if len(order) == node:
    print(*order)
else: print('Cannot complete these tasks. Going to bed.')