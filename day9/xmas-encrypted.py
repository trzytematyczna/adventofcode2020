with open("input") as f:
    fpass = f.readlines()

codes = list(map(lambda x: int(x.strip()), fpass))

preamble = 25

def checksum(relative_start,relative_end,num):
    for fi in range(relative_start,relative_end+1):
        for si in range(fi,relative_end+1):
            if codes[fi] + codes[si] == num:
                return True
    return False


for i in range(preamble,len(codes)):
    if not checksum((i-preamble),(i-1),codes[i]):
        print(codes[i])


#85848519