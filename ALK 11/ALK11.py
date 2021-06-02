class Node:
    def __init__(self, id):
        self.id = id
        self.neighbours = []

    def setNeighbours(self, dest_id, cost):
        x = [self.id, dest_id, cost]
        self.neighbours.append(x)


def bubble_sort(queue):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(queue) - 1):
            if queue[i][2] > queue[i + 1][2]:
                queue[i], queue[i + 1] = queue[i + 1], queue[i]
                swapped = True


if __name__ == "__main__":
    # Input
    n = int(input("number of vertices: "))
    nodes = []
    totalcost = 0

    for i in range(0, n + 1):
        nodes.append(Node(i))

    p = int(input("number of edges: "))

    print("fill in all edges in form: 'v1 v2 cost' divided with spaces")
    print("eg. set '1 2 10' is an edge between v1 and v2 and cost 10")

    print("edges: ")
    for i in range(0, p):
        edge = input().split(' ')
        edge = [int(x) for x in edge]

        nodes[edge[0]].setNeighbours(edge[1], edge[2])
        nodes[edge[1]].setNeighbours(edge[0], edge[2])

    queue = []
    final_edges = []

    tree = [1]
    current_node = 1
    check = True

    while len(tree) < n:
        if check:
            # add edges to queue
            pom = nodes[current_node].neighbours
            for c in pom:
                queue.append(c)
            bubble_sort(queue)
        else:
            check = True
            check1 = True
            check2 = True

        # get best edge
        current_edge = queue[0]
        del queue[0]

        # check if edge goes to new v, we only look for dest, because we know we came from known v
        for i in tree:
            if i == current_edge[1]:
                check = False

        # if edge goes to a new vertice
        if check:
            tree.append(current_edge[1])
            final_edges.append([current_edge[0], current_edge[1]])
            totalcost += int(current_edge[2])
            current_node = current_edge[1]

    print("Total cost: ", totalcost)
    print("Final edges: ")
    for i in final_edges:
        print(i)
