import re
f = open('input.txt', 'r')

passlists = []
passport = {}
for line in f.readlines():
    if not line=='\n' :
        # splitted = line.strip().split(" ")
        splitted = line.split(" ")
        for s in splitted:
            m = re.search('([a-z]{3}):(.*)', s)
            passport[m.groups()[0]] = m.groups()[1]
            # key, value = s.split(":")
            # passport[key] = value
    else:
        passlists.append(passport)
        passport = {}
passlists.append(passport)
f.close()

valid = 0

for d in passlists:
    if d.keys() >= {"byr","iyr", "eyr", "hgt", "hcl", "ecl","pid"}:
        valid += 1

#print(len(passlists))
print(valid)
#847