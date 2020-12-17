
def readdata():
    f = open('input', 'r')

    sl = []
    for line in f.readlines():
        if not line == '\n':
            l = list(line.strip())
            sl.append(l)
    f.close()
    # print(sl)
    return sl

def how_occupied(rp, cp, rpmax, cpmax, sl):
    c = 0
    inds = [(rp, cp - 1), (rp - 1, cp - 1), (rp + 1, cp - 1),(rp - 1, cp), (rp + 1, cp), (rp, cp + 1), (rp - 1, cp + 1), (rp + 1, cp + 1)]

    # print(rp,cp,inds)
    for i in inds:
        if not (i[0] < 0 or i[0] >= rpmax or i[1] < 0 or i[1] >= cpmax):
            if sl[i[0]][i[1]] == "#":
                c += 1
                # print(i, sl[i[0]][i[1]])
    return c


def turn(seat_map,occ_max):
    copy_seat_map = copy_map(seat_map)
    # map = in_map
    rmax = len(copy_seat_map)
    cmax = len(copy_seat_map[0])

    change = False
    for r in range(0, rmax):
        for c in range(0, cmax):
            # cpy_seatlist = map[r]
            if copy_seat_map[r][c] == ".":
                continue
            elif copy_seat_map[r][c] == "L" and how_occupied(r, c, rmax, cmax, copy_seat_map) == 0:
                seat_map[r][c] = "#"
                change = True
            elif copy_seat_map[r][c] == "#" and how_occupied(r, c, rmax, cmax, copy_seat_map) >= occ_max:
                seat_map[r][c] = "L"
                change = True
            #map=cpy_seatlist
    return change

def print_map(map):
    for row in map:
        print("".join(row))

def copy_map(map):
    new_map = []
    for row in map:
        new_map.append(row.copy())
    return new_map


def count_occupied(sl):
    occ = 0
    for i in sl:
        occ += i.count('#')
    return occ


# seatlist = readdata()
# changeson = True
# counter = 0
# print_map(seatlist)
# occupied_max=4
# while (changeson):
#     counter += 1
#     changeson = turn(seatlist,occupied_max)
#     print('\n>> After turn %d\n' % counter)
#     # print_map(seatlist)
#
# print(count_occupied(seatlist))


def turn_new_rules(seat_map,occ_max):
    copy_seat_map = copy_map(seat_map)
    rmax = len(copy_seat_map)
    cmax = len(copy_seat_map[0])

    diag_back = find_diags(copy_seat_map, False)
    diag_forw = find_diags(copy_seat_map, True)
    cols = find_cross(copy_seat_map, True)
    rows = find_cross(copy_seat_map, False)

    change = False
    for r in range(0, rmax):
        for c in range(0, cmax):
            # print(r,c,how_occupied_new_rules(r, c, copy_seat_map[r][c],copy_seat_map))
            num_occupied = how_occupied_new_rules(r, c, copy_seat_map[r][c], diag_back,diag_forw,cols,rows)
            if copy_seat_map[r][c] == "L" and num_occupied == 0:
                seat_map[r][c] = "#"
                change = True
            elif copy_seat_map[r][c] == "#" and num_occupied >= occ_max:
                seat_map[r][c] = "L"
                change = True
    return change



def how_occupied_new_rules(rp, cp,val, diag_back,diag_forw,cols,rows):
    occupied = 0

    diag_particular_back = find_particular(diag_back, rp, cp, val)
    particular_index = diag_particular_back.index((rp, cp, val))
    occupied += occupied_in_list_both_sides(diag_particular_back, particular_index)
    # print("occ:",occupied)

    diag_particular_for = find_particular(diag_forw, rp, cp, val)
    particular_index = diag_particular_for.index((rp, cp, val))
    occupied += occupied_in_list_both_sides(diag_particular_for, particular_index)
    # print("occ:",occupied)

    cross_col = find_particular(cols, rp, cp, val)
    particular_index = cross_col.index((rp, cp, val))
    occupied += occupied_in_list_both_sides(cross_col, particular_index)
    # print("occ:",occupied)

    cross_row = find_particular(rows, rp, cp, val)
    particular_index = cross_row.index((rp, cp, val))
    occupied += occupied_in_list_both_sides(cross_row, particular_index)
    # print("occ:",occupied)


    return occupied


def find_diags(test, f):
    max_col = len(test[0])
    max_row = len(test)
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            fdiag[x + y].append((y,x,test[y][x])) #x= column,  y= row
            bdiag[x - y - min_bdiag].append((y,x,test[y][x]))
    if f:
        return fdiag
    else:
        return bdiag

def find_particular(tabs, rindex, cindex, val):
    for d in tabs:
        # Monis
        for tup in d:
            if tup[0] == rindex and tup[1] == cindex:
                return d
        # Patrys
        for x, y, _ in d:
            if x == rindex and y == cindex:
                return d


def find_cross(test, c):
    max_col = len(test[0])
    max_row = len(test)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append((y,x,test[y][x]))
            rows[y].append((y,x,test[y][x]))
    if c:
        return cols
    else:
        return rows


def occupied_in_list_both_sides(sel, sel_index):
    before = sel[:sel_index].copy()
    before.reverse()
    after = sel[sel_index+1:].copy()
    c = 0

    for pos in range(len(after)):
        seat = after[pos][2]
        if seat == "#":
            c += 1
        if seat != ".":
            break

    for pos in range(len(before)):
        seat = before[pos][2]
        if seat == "#":
            c += 1
        if seat != ".":
            break
    return c

seatlist = readdata()
changeson = True
counter = 0
# print_map(seatlist)
occupied_max=5
while (changeson):
    counter += 1
    changeson = turn_new_rules(seatlist,occupied_max)
    print('\n>> After turn %d\n' % counter)
    # print_map(seatlist)

print(count_occupied(seatlist))
