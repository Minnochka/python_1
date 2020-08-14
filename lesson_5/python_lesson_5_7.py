import json

try:
    with open("firms.txt", "r", encoding="utf-8") as file:
        t = file.read().splitlines()
    print(t)
    cnt =0
    summ = 0
    d = {}
    for firm in t:
        firm_info = firm.split()
        #print(subject_info)
        firm_name = firm_info[0]
        revenue = float(firm_info[2])
        cost = float(firm_info[3])
        profit = revenue - cost
        if profit > 0:
            cnt += 1
            summ += profit
        #print(s)
        d[firm_name] = profit

    if cnt > 0:
        res = [d, {"average_profit": round(summ / cnt, 2)}]
    else:
        res = [d, {"average_profit": 0}]
        
    print(d)
    print(res)

    with open("firms_res.txt", "w", encoding="utf-8") as file_n:
        json.dump(res, file_n)
    
except FileNotFoundError:
    print("File not found! Please, create file.")
