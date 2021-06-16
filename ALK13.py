import sys


class Node:
    def __init__(self, id):
        self.id = id
        self.neighbours = {}
        self.visited = False

    def setNeighbours(self, dest_id, cost):
        self.neighbours[dest_id] = cost


def print_path(G, s, v):
    if v == s:
        print(s)
    elif v.pi == -1:
        print("brak ścieżki")
    else:
        print(v)


if __name__ == "__main__":
    V = [0]
    E = []
    d = [0, 0]
    p = [0]
    B = {}

    # input Vertices
    k = int(input("|V|: "))

    for i in range(1, k + 1):
        new = Node(i)
        V.append(new)

    # input Edges
    n = int(input("|E| = "))
    print("edge input: v1 v2 omega")
    for i in range(0, n):
        edge = input().split(' ')
        edge = [int(x) for x in edge]

        V[edge[0]].setNeighbours(edge[1], edge[2])
        V[edge[1]].setNeighbours(edge[0], edge[2])

    for i in range(1, k+1):
        d.append(sys.maxsize)
        p.append(0)
        B[i] = d[i]

while len(B) > 0:
    # get index of first element of B
    k = next(iter(B))
    B.pop(k)

    # for all neighbours do the magic
    for i in list(V[k].neighbours.keys()):

        if d[k] + int(V[k].neighbours[i]) < d[i]:
            d[i] = d[k] + V[k].neighbours[i]
            p[i] = k

            # Priority Q
            if i in B:
                B[i] = d[k] + V[k].neighbours[i]
                B = dict(sorted(B.items(), key=lambda c: c[1]))


for i in range(1, k+1):
    result = []
    j = i
    while j != 0:
        result.append(j)
        j = p[j]
    result = result[::-1]
    print(i, result)
