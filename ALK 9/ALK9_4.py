def Podział(n, b, m, a, k):
    sub = []
    if n == 0:
        for i in range(1, m + 1):
            sub.append(a[i])
        sub.insert(0, int(k))
        Sprzężenie(sub)
    else:
        for i in range(1, (min(b, n) + 1)):
            a[m + 1] = i
            Podział(n - i, i, m + 1, a, k)


def Sprzężenie(tab):
    sub = []
    for i in range(0, tab[0]):
        sub.append(1)

    for i in range(1, len(tab)):
        for j in range(0, tab[i]):
            sub[j] += 1

    print("podział sprzężony: ", sub)


if __name__ == "__main__":
    n = int(input("n: "))
    k = int(input("k: "))

    a = []
    b = n
    m = 0
    for i in range(1, n+1):
        a.append(int(0))
    Podział(n-k, b-k, m, a, k)
