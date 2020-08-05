def my_func(num_1, num_2):
    try:
        res = round(float(num_1) / float(num_2), 4)
        return (res, "OK")
    except ZeroDivisionError:
        return(-2, "You can't use 0 as second number!")
    except ValueError:
        return(-1, "Use only numbers!")

while True:
    key = input("Enter 'end' for exit or press any key: ")
    if key == 'end':
        break
    res = my_func(input("Enter first number: "), input("Enter second number: "))
    if res[1] == "OK":
        print("Result: {}".format(res[0]))
    else:
        print("Error: {}".format(res[1]))
