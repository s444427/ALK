if __name__ == "__main__":
    n = int(input("n: "))
    parity = True
    x = []

    for i in range(0, n):
        x.append(0)

    for j in range(0, pow(2, n)):
        sub = []
        if not parity:
            x[-1] = (x[-1]+1) % 2
        else:
            for i in range(n-1, 0, -1):
                if x[i] == 1:
                    x[i-1] = (x[i-1]+1) % 2
                    break
        parity = not parity

        for k in range(0, n):
            sub.append((k+1)*x[k])
        sub = [p for p in sub if p != 0]
        print(sub)

