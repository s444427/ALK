def getTree(L):
    edges = []
    d = []
    n = len(L) + 2

    for c in range(0, n):
        d.append(int(1))

    for i in L:
        d[int(i - 1)] += 1
    L.insert(n, 1)

    for i in range(0, n - 1):
        true = 0
        c = n - 1
        while true == 0:
            if d[c] == 1:
                print([L[i], c + 1])
                edges.append([L[i], c + 1])
                d[L[i] - 1] -= 1
                d[c] -= 1
                true = 1
            else:
                c -= 1


if __name__ == "__main__":

    y = input("Podaj kod prufera rozdzielony przecinkami: ").split(',')
    p = [int(x) for x in y]
    getTree(p)
