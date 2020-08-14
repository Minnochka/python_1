try:
    with open("employees.txt", "r", encoding="utf-8") as my_file:
        strs = my_file.read().splitlines()
    if len(strs) == 0:
        print("Список сотрудников пуст!")
    else:
        print("Оклад меньше 20 тыс:")
        sum_money = 0
        for e in strs:
            emp = e.split()
            if float(emp[1]) < 20000:
                print(emp[0])
            sum_money += float(emp[1])
        print("Средний оклад сотрудника: {}".format(round(sum_money/len(strs), 2)))
except FileNotFoundError:
    print("File not found! Please, create file.")
