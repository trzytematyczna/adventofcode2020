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

#     byr (Birth Year) - four digits; at least 1920 and at most 2002.
#     iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#     eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#     hgt (Height) - a number followed by either cm or in:
#         If cm, the number must be at least 150 and at most 193.
#         If in, the number must be at least 59 and at most 76.
#     hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#     ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#     pid (Passport ID) - a nine-digit number, including leading zeroes.
#     cid (Country ID) - ignored, missing or not.

def is_valid(d):
    if not 1920 <= int(d["byr"]) <= 2002:
        return False
    if not 2010 <= int(d["iyr"]) <= 2020:
        return False
    if not 2020 <= int(d["eyr"]) <= 2030:
        return False
    hgt = re.match('^([0-9]{2,3})(cm|in)$',d["hgt"])
    if hgt is None:
        return False
    if hgt.groups()[1] == "cm":
        if not 150 <= int(hgt.groups()[0]) <= 193:
            return False
    else:
        if not 59 <= int(hgt.groups()[0]) <= 76:
            return False
    if re.match('^#[0-9a-z]{6}$',d["hcl"]) is None:
        return False
    if d["ecl"] not in {"amb","blu","brn","gry","grn","hzl","oth"}:
        return False
    if re.match('^[0-9]{9}$', d["pid"]) is None:
        return False
    return True

ok_pass = 0
valid = 0
for d in passlists:
    if d.keys() >= {"byr","iyr", "eyr", "hgt", "hcl", "ecl","pid"}:
        ok_pass += 1
        if(is_valid(d)):
            valid += 1

print(ok_pass)
print(valid)
#847