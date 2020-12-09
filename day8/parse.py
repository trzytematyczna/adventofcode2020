import re
import pandas as pd
f = open('input', 'r')

data=[]
for line in f.readlines():
    if not line=='\n' :
        m = re.search('(acc|jmp|nop) ([-|+]?[0-9]+)', line.strip())
        data.append([m.groups()[0],int(m.groups()[1])])
f.close()
ops = pd.DataFrame(data,columns=["operation","stride"])

# visited=set()
# i = 0
# accumulator = 0
# c = ops["operation"][i]
# while i not in visited:
#     if c == "acc":
#         visited.add(i)
#         accumulator += ops["stride"][i]
#         i += 1
#     elif c == "jmp":
#         visited.add(i)
#         j = ops["stride"][i]
#         i += j
#     elif c == "nop" :
#         visited.add(i)
#         i += 1
#
#     c = ops["operation"][i]
#
# print(accumulator)


def is_loopy(ops_list):
    visited = set()
    i = 0
    c = ops_list["operation"][i]
    acc = 0
    while i not in visited:
        visited.add(i)
        if c == "acc":
            acc += ops_list["stride"][i]
            i += 1
        elif c == "jmp":
            jn = ops_list["stride"][i]
            i += jn
        elif c == "nop":
            i += 1

        if i >= len(ops_list):
            return acc

        c = ops_list["operation"][i]

    return -1

jmp_idx = ops.index[ops['operation'] == 'jmp']
nop_idx = ops.index[ops['operation'] == 'nop']

for j in jmp_idx:

    ops.loc[j, "operation"] = "nop"
    r = is_loopy(ops)
    if r != -1:
        print("jmp acc value:", r)
    ops.loc[j, "operation"] = "jmp"

for n in nop_idx:
    ops.loc[n,"operation"] = "jmp"
    p = is_loopy(ops)
    if p != -1:
        print("nop acc value:",p)
    ops.loc[n, "operation"] = "nop"
