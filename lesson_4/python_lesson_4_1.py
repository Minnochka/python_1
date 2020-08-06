from sys import argv

def salary_f(hours, money_by_hour, bonus):
    if hours.isdigit():
        hours = int(hours) 
    else:
        return "Hour is number and >0!"
    try:
        money_by_hour = float(money_by_hour)
        if (money_by_hour <= 0):
            return "Money for hour > 0!"
    except ValueError:
        return "Money for hour is number!"
    try:
        bonus = float(bonus)
        if (bonus < 0):
            return "Bonus >= 0!"
    except ValueError:
        return "Bonus is number!"
    return "Salary = {}".format(round((hours * money_by_hour) + bonus, 2))

name, hours, money_by_hour, bonus = argv
print(salary_f(hours, money_by_hour, bonus))
