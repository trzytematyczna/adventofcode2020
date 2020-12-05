
import functools as ft
import re, operator

with open("input.txt") as f:
    fpass = f.readlines()
#fpass = pd.read_table("input.txt")

clearfun = lambda x: x.strip(   )
cpass = list(map(clearfun, fpass))

validpass = 0
validpass2 = 0
for p in cpass:
    m = re.search('([0-9]+)-([0-9]+) ([a-z]+): ([a-z]+)', p)
    lower = m.groups()[0]
    upper = m.groups()[1]
    pchar = m.groups()[2]
    passstring = m.groups()[3]

    char_occurrence = passstring.count(pchar)
    if char_occurrence >= int(lower) and char_occurrence <= int(upper) :
        validpass += 1

    if operator.xor((passstring.find(pchar, int(lower) - 1, int(lower)) != -1), (passstring.find(pchar, int(upper) - 1, int(upper)) != -1)):
            validpass2 += 1


print(validpass)
print(validpass2)

#word = "dooobiedoobiedoobie"
#match = 'o'
#ft.map(lambda count, char: count + 1 if char == match else count, word, 0)
