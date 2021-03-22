st = "BWWWWWBWWWWSSSSSYYYHKKK"
res = ""
last = st[0]
number = 0
for i, alb in enumerate(st):
    if last != alb:
        res += str(number) + last
        last = alb
        number = 1
    elif i == len(st)-1:
        number += 1
        res += str(number) + last
    else:
        number += 1

print(res)

res1 = ""
s = 0
str_num = ""
for s in range(len(res)):
    if res[s].isalpha():
        res1 += int(str_num) * res[s]
        str_num = ""
    else:
        str_num += res[s]

print(res1)

