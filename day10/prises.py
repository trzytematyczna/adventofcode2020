
with open("input") as f:
    fpass = f.readlines()

prises = list(map(lambda x: int(x.strip()), fpass))

prises.insert(0,0)
prises.append(max(prises)+3)
prises.sort()

diffs = [t - s for s, t in zip(prises, prises[1:])]

diffs.count(1)
diffs.count(3)
ones = len(list(filter(lambda x: x == 1, diffs)))
threes = len(list(filter(lambda x: x == 3, diffs)))

print(ones*threes)


import networkx as nx


g = nx.DiGraph()

for i in range(0,len(prises)):
    n_i = prises[i]
    print(n_i)
    g.add_node(n_i)
    j = i+1
    while j < len(prises):
        print(i,j)
        n_j = prises[j]
        if n_j-n_i <= 3:
            g.add_edge(n_i,n_j)
            print("add ",i,j)
        j += 1


topological = list(reversed(list(nx.topological_sort(g))))
print(topological)


def pathsnum(tops):
    dp = {}
    for n in tops:
        if n == tops[0]:
            dp[n] = 1
        else:
            dp[n] = 0
    for n in tops:
        for suc in g.successors(n):
            dp[n]+=dp[suc]

    return dp[0]

# print(list(nx.topological_sort(nx.line_graph(g))))
print(g.nodes)
print(g.edges)
#187916557893772
# 184473632
# 49607173328384
print(pathsnum(topological))