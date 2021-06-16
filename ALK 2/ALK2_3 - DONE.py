def ALG(x, i):
    if i == n-1:
        print(list(x.values()))
    else:
        for j in range(1, k + 1):
            x[i + 1] = j
            ALG(x, i + 1)


if __name__ == "__main__":
    x = {}

    n = int(input("n: "))
    k = int(input("k: "))

    ALG(x, 0)
