n = int(input("n: "))
xlist = []
baselist = []
finallist = []
end = 0
printable = 0

for j in range(0, n):
    xlist.append(0)

for y in range(1,n+1):
    baselist.append(y)

while end < n:
    # print(xlist)
    end = 0
    finallist = []

    # Print
    for i in range(0, n):
        if xlist[i] == 1:
            finallist.append(baselist[i])
    print(finallist)

    # Add 1
    xlist[-1] += 1

    # Check overflow
    for a in range(n - 1, 0, -1):
        if (xlist[a]) == 2:
            for c in range(a, n):
                xlist[c] = 0
            xlist[a - 1] += 1

    # Check if end now
    for b in range(0, n):
        if xlist[b] == 1:
            end += 1

finallist = []
# Print
for i in range(0, n):
    if xlist[i] == 1:
        finallist.append(baselist[i])
print(finallist)