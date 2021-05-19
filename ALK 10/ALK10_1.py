class Node:
    def __init__(self):
        self.neighbours = []
        self.degree = 0

    def getNeighbours(self):
        return str(self.neighbours)

    def setNeighbours(self, x):
        self.neighbours.append(x)
        self.degree += 1

    def getDegree(self):
        return int(self.degree)


def getPrufer(nodes):
    prufer = []
    degrees = []
    for i in nodes:
        degrees.append(i.getDegree())

    for k in range(0, n - 2):
        i = n
    true = 0
    while true == 0:
        if degrees[i] == 1:
            neighbour = int(nodes[i].getNeighbours()[1])
            prufer.append(neighbour)

            degrees[neighbour] -= 1
            degrees[i] -= 1

            true = 1
        else:
            i -= 1
    return prufer


if __name__ == "__main__":
    # Input
    n = int(input("n: "))
    edges = []
    nodes = []

    for i in range(0, n + 1):
        nodes.append(Node())

    print("edges: ")
    for i in range(0, n - 1):
        edge = input().split(' ')
        edge = [int(x) for x in edge]
        edges.append(edge)

        nodes[edge[0]].setNeighbours(edge[1])
        nodes[edge[1]].setNeighbours(edge[0])

    # Prufer from tree
    print(getPrufer(nodes))


