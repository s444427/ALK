def P(n, k):
    if n == 0 and k == 0:
        return int(1)
    elif n > 0 and k == 0:
        return int(0)
    elif k <= n:
        return int(P(n - 1, k - 1) + P(n - k, k))
    else:
        return 0


if __name__ == "__main__":
    n = int(input("n: "))
    k = int(input("k: "))
    print("P(n, k) = ", P(n, k))
