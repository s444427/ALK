class Edge:
    def __init__(self, V, u, v, omega):
        self.u = int(V[u - 1].id)
        self.v = int(V[v - 1].id)
        self.omega = omega


class x:
    def __init__(self):
        self.id = 0
        self.p = 0
        self.rank = 0

    def MAKE_SET(self):
        self.p = self
        self.rank = 0
        return 0

    def FIND_SET(self):
        if self != self.p:
            self.p = self.p.FIND_SET()
        return self.p


def UNION(V, x, y):
    LINK(V[x - 1].FIND_SET(), V[y - 1].FIND_SET())


def LINK(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1


def sort_wages(E):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(E) - 1):
            if E[i].omega > E[i + 1].omega:
                E[i], E[i + 1] = E[i + 1], E[i]
                swapped = True


def MST_KRUSKAL(E, V):
    F = []
    for u in V:
        u.MAKE_SET()
    sort_wages(E)  # niemalejąco względem wag omega
    for single_edge in E:
        u = single_edge.u
        v = single_edge.v
        if V[u - 1].FIND_SET() != V[v - 1].FIND_SET():
            F.append(single_edge)
            UNION(V, u, v)
    return F


if __name__ == "__main__":
    V = []
    E = []
    k = int(input("|V|: "))

    for i in range(1, k + 1):
        new = x()
        new.id = int(i)
        V.append(new)

    n = int(input("|E| = "))
    print("edge input: v1 v2 omega")
    for i in range(0, n):
        u, v, omega = input("edge "+str(i+1)+". ").split()
        edge = Edge(V, int(u), int(v), int(omega))
        E.append(edge)

    result = MST_KRUSKAL(E, V)
    suma = 0
    for i in result:
        print(i.u, i.v)
        suma += i.omega
    print("total cost: ", suma)
