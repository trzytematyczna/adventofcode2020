import re
from networkx.algorithms.simple_paths import all_simple_paths
import networkx as nx

with open("input2") as f:
    fpass = f.readlines()

bag_rules = list(map(lambda x: x.strip(), fpass))

#mirrored indigo bags contain 4 pale tan bags, 1 posh indigo bag, 3 shiny salmon bags, 4 wavy indigo bags.
# bag_rules=bag_rules[1:2]
better_rules = nx.DiGraph()
# bag_rules=bag_rules[0:3]

for rule in bag_rules:
    # m = re.match("([a-z]+ [a-z]+) bags contain ([0-9]+ [a-z]+ [a-z]+) [bag|bags]",rule)
    # print(rule)
    splited_rule=rule.replace('bags','bag').replace('contain ','').split(" bag")
    splited_rule = list(map(str.strip, splited_rule))
    rls = list(map(lambda x: x.replace(", ", "").replace('.', ""), splited_rule))
    rls = list(filter(None, rls))

    node_m=rls[0]
    better_rules.add_node(node_m)

    for r in rls[1:]:
        g = re.match("([0-9]+) ([a-z]+ [a-z]+)", r)
        if g is not None:
            node_r = g.groups()[1]
            w = g.groups()[0]
            better_rules.add_edge(node_m,node_r,weight=w)

def bagpath(bagfrom, bagto):
    p = []
    for path in all_simple_paths(better_rules, bagfrom, bagto):
        p.append(path)
        # print(p)
    return p


# print(better_rules.edges)
# print(better_rules.nodes)
elist = []
for i in better_rules.nodes:
    # print(i)
    if i != "shiny gold":
        w = bagpath(i,"shiny gold")
        if w is not None:
            elist.extend(w)

a = nx.algorithms.ancestors(better_rules,"shiny gold")
print(len(a))
flattened_list = [y for x in elist for y in x]
myset = set(flattened_list).difference({"shiny gold"})
print(len(myset))


def weightme(bagfrom, bagto):
    sum_paths = 0
    added_edges = set()
    for path in all_simple_paths(better_rules, bagfrom, bagto):
        p = 1
        q = 0
        for m in range(0,len(path)-1):
            print(path[m],path[m+1],":",better_rules.get_edge_data(path[m],path[m+1])["weight"])
            current_weight = int(better_rules.get_edge_data(path[m], path[m + 1])["weight"])
            print(q, p)
            p *= current_weight
            if m != len(path)-2 and ((path[m], path[m + 1]) not in added_edges):
                added_edges.add((path[m], path[m + 1]))
                q += current_weight
        print(path,q,p)
        print(added_edges)
        sum_paths = sum_paths + p + q
    return sum_paths

endnodes = (node for node, out_degree in better_rules.out_degree() if out_degree == 0)

sum_weight = 0
for i in endnodes:
    w = weightme("shiny gold",i)
    print(i)
    if w is not None:
        sum_weight += w
print(sum_weight)

# 51558
# 52420
# 52283

