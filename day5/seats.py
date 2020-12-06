import re
from typing import List


def sort_seats(seatstr: List, min_index: int, max_index: int) -> int:
    if min_index >= max_index:
        # print("exiting:", min_index)
        return int(min_index)

    # print(seatstr)
    c = seatstr[0]
    nrange = ((max_index - min_index)+1) / 2
    # print(nrange)
    if c == "L" or c == "F":
        min_index = min_index
        max_index = min_index + nrange - 1
        # print("aF:",min_index,max_index)
    if c == "R" or c == "B":
        max_index = max_index
        min_index = max_index - nrange + 1
        # print("aB:", min_index, max_index)
    # print("asd:", min_index, max_index)
    return sort_seats(seatstr[1:], min_index, max_index)


with open("input") as f:
    fpass = f.readlines()

seat_list = list(map(lambda x: x.strip(), fpass))

# seat_list = ["FBFBBFFRLR"]
row_max, col_max = 0,0
ids = []
for s in seat_list:
    m = re.match("([F|B]+)([LR]+)",s)

    seat_row_string = m.groups()[0]
    # print(seat_row_string, len(seat_row_string), 2**len(seat_row_string))
    seat_row = sort_seats(seat_row_string, 0, (2**len(seat_row_string))-1)
    # print("row: ",seat_row)

    seat_col_string = m.groups()[1]
    # print(seat_col_string, len(seat_col_string), 2**len(seat_col_string))
    seat_col = sort_seats(seat_col_string, 0, (2**(len(seat_col_string)) - 1))
    # print("col: ",seat_col)

    ids.append(seat_row*8+seat_col)
    if(seat_row>row_max):
        row_max = seat_row
        col_max = seat_col
    if(seat_row == row_max and seat_col > col_max):
        row_max = seat_row
        col_max = seat_col

print(row_max*8+col_max)

ids.sort()

fullid = set(range(min(ids), max(ids)+1))

myid=fullid.difference(ids)

print(myid)

# function merge_sort(list m) is
#     // Base case. A list of zero or one elements is sorted, by definition.
#     if length of m ≤ 1 then
#         return m
#
#     // Recursive case. First, divide the list into equal-sized sublists
#     // consisting of the first half and second half of the list.
#     // This assumes lists start at index 0.
#     var left := empty list
#     var right := empty list
#     for each x with index i in m do
#         if i < (length of m)/2 then
#             add x to left
#         else
#             add x to right
#
#     // Recursively sort both sublists.
#     left := merge_sort(left)
#     right := merge_sort(right)
#
#     // Then merge the now-sorted sublists.
#     return merge(left, right)