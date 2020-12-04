

import pandas as pd
import numpy

f = pd.read_table('input-file.txt', header = None)
expense = numpy.array(f)

# a = numpy.array([[1],[2]])
# b = numpy.array([[2],[3]])
# c = numpy.add.outer(a, b)
# print(c,'\n')
# print(numpy.isin(c, 5).nonzero())

# added[(31,0,174,0)]
added = numpy.add.outer(expense, expense)
val = 2020

# returns array with values of indexes for expense array, where the values are
# (array([ 31, 174]), array([0, 0]), array([174,  31]), array([0, 0]))
indexes_in_expense = numpy.isin(added, val).nonzero()

# added[(31,0,174,0)] this indeed equals 2020
index1 = indexes_in_expense[0][0]
index2 = indexes_in_expense[2][0]

res1 = expense[index1, ]
res2 = expense[index2, ]

print(index1,index2)
print(res1 * res2)

####

added3 = numpy.add.outer(added, expense)
val = 2020

# returns array with values of indexes for expense array, where the values are
# (array([ 61, 61, 134, 134, 170, 170]), array([0, 0, 0, 0, 0, 0]), array([134, 170,  61, 170,  61, 134]), array([0, 0, 0, 0, 0, 0]), array([170, 134, 170,  61, 134,  61]), array([0, 0, 0, 0, 0, 0]))
indexes_in_expense3 = numpy.isin(added3, val).nonzero()
print(indexes_in_expense3)

index31 = indexes_in_expense3[0][0]
index32 = indexes_in_expense3[2][0]
index33 =  indexes_in_expense3[4][0]

res31 = expense[index31]
res32 = expense[index32]
res33 = expense[index33]
print(index31, index32, index33)
print(res31*res32*res33)