def my_func(num_1, num_2, num_3):
    try:
        l = [float(num_1), float(num_2), float(num_3)]
    except ValueError:
        return "Only numbers!"
    first = max(l)
    l.remove(first)
    return first + max(l)
    
while True:
    if input("Enter 'end' for exit or any symbol for continue: ") == 'end':
        break
    res = my_func(input("Enter first number: "), input("Enter second number: "), input("Enter third number: "))
    print("Result: {}".format(res))
