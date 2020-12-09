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

wrong = 0
for i in range(preamble,len(codes)):
    if not checksum((i-preamble),(i-1),codes[i]):
        wrong = codes[i]


# 85848519

for start in range(0,len(codes)):
    for step in range(2, len(codes)+1):
        if sum(codes[start:step])==wrong and codes[start:step]!=[wrong]:
            print("contiguous set of at least two numbers:",codes[start:step])
            print(min(codes[start:step])+max(codes[start:step]))
# 13414198