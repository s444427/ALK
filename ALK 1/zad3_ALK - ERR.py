n = int(input("n: "))
k = int(input("k: "))
xlist = []
end = 0
printable = 0

for j in range(0, n):
    xlist.append(1)

while end < n:
    # print("Siemka")
    # print(xlist)
    end = 0
    printable = 0

    # Check if print
    for d in range(1, n):
        if xlist[d - 1] >= xlist[d]:
            printable += 1

    if printable == 0:
        # Print
        x = ""
        for i in range(0, n):
            x = x + str(xlist[i])
        print(x)

    # Add 1
    xlist[-1] += 1

    # Check overflow
    for a in range(n - 1, 0, -1):
        if (xlist[a] - 1) / k == 1:
            xlist[a] = xlist[a - 1]
            xlist[a - 1] += 1

    # Check if end now
    for b in range(0, n):
        if xlist[b] >= k - n + b + 1:
            end += 1

if k != 1:
    x = ""
    for i in range(0, n):
        x = x + str(xlist[i])
    print(x)
