from graph import Graph

g = Graph("graph18.txt")
n = g.get_node_list()
print(n)

for i in n:
    for j in n:
        print(i, ', ', j, ': ', g.get_weight(i, j))