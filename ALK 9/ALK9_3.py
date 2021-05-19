def Podział(n, b, m, a):
    sub = []
    if n == 0:
        for i in range(1, m+1):
            sub.append(a[i])
        print(sub)
    else:
        for i in range(1, (min(b, n) + 1)):
            a[m+1] = i
            Podział(n - i, i, m + 1, a)


if __name__ == "__main__":
    a = []
    n = int(input("n: "))
    b = n
    m = 0
    for i in range(0, n+1):
        a.append(int(0))
    Podział(n-3, b-3, m, a)
