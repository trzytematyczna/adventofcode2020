
with open("input.txt") as f:
    fpass = f.readlines()

clearfpass = lambda x: x.strip()
treemap = list(map(clearfpass, fpass))

tree_nb = 0
step = 0
for l in treemap[1:]:
    step += 3
    if(step>=len(l)):
        step = step - len(l)
    if(l[step]=="#"):
        tree_nb += 1

print(tree_nb)

def go(step):
    tree_nb = 0
    step_it = 0
    for l in treemap[1:]:
        step_it += step
        if(step_it>=len(l)):
            step_it = step_it - len(l)
        if(l[step_it]=="#"):
            tree_nb += 1
    return(tree_nb)


def jumpygo(step):
    tree_nb = 0
    step_it = 0
    jump = True
    for l in treemap[1:]:
        if not jump:
            step_it += step
            if step_it>=len(l):
                step_it = step_it - len(l)
            if l[step_it] == "#":
                tree_nb += 1
            jump = True
        else:
            jump = False
    return(tree_nb)

print(go(1),go(3),go(5),go(7),jumpygo(1))
print(go(1)*go(3)*go(5)*go(7)*jumpygo(1))
#
# 83 81 76 76 43
# 1669778064
# 1553281920
# 1708610112