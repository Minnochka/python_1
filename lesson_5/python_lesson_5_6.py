import re
from functools import reduce

d = {}
try:
    with open("subjects.txt", "r", encoding="utf-8") as file:
        t = file.read().splitlines()
    #print(t)
    for sub in t:
        subject_info = sub.split()
        #print(subject_info)
        sub_name = subject_info[0]
        hours = re.findall(r'\d+', sub)
        if len(hours) != 0:
            s = reduce(lambda x,y: x + y, [int(el) for el in hours])
        else:
            s = 0
        #print(s)
        d[sub_name] = s
    print(d)
except FileNotFoundError:
    print("File not found! Please, create file.")
