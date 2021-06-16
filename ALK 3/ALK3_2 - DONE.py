if __name__ == "__main__":
    n = int(input("n: "))
    T = input("T format '1 3': ").split()

    x = []
    for i in range(0, n + 1):
        x.append(0)

    for i in T:
        x[int(i)] = 1

    for i in range(1, n + 1):
        x[i] = (x[i - 1] + x[i]) % 2

    base = 1
    r = 0
    for i in range(n, 0, -1):
        r += x[i] * base
        base *= 2

    print(r)
