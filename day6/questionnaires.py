import re
f = open('input', 'r')

group_answer = ""
questionnaires_list = []
for line in f.readlines():
    if not line == '\n' :
        group_answer += line.strip()
    else:
        questionnaires_list.append(group_answer)
        group_answer = ""
questionnaires_list.append(group_answer)
f.close()

def unique_chars_number(str):
    return len(list(set(str)))

sum_all = 0
for q in questionnaires_list:
    sum_all += unique_chars_number(q)

print(sum_all)

########### 2nd part

f = open('input', 'r')

group_answer = []
questionnaires_list = []
for line in f.readlines():
    if not line == '\n' :
        group_answer.append(line.strip())
    else:
        questionnaires_list.append(group_answer)
        group_answer = []
questionnaires_list.append(group_answer)
f.close()

print(questionnaires_list)

sum_all = 0
for q in questionnaires_list:
    setint = set(q[0])
    for i in range(1,len(q)):
        setint = setint.intersection(set(q[i]))
    sum_all += len(setint)

print(sum_all)

##alternative 2nd part
sum_all=0
for q in questionnaires_list:
    l1 = list(map(lambda x: set(x), q))
    sum_all += len(set.intersection(*l1))
print(sum_all)
