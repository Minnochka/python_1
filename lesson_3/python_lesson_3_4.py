def degree(x, y):
    if y == 1:
        return x
    else:
        return degree(x, y - 1) * x
    
    
def minus(x, y):
    return 1 / degree(x, abs(y))

while True:
    if input("Enter 'end' for exit or any symbol for continue: ") == 'end':
        break
    try:
        x = float(input("Enter x (x > 0): "))
    except ValueError:
        print("X not number!")
        continue
    if x <= 0:
        print("X > 0!")
        continue
    try:
        y = int(input ("Enter y (y < 0): "))
    except ValueError:
        print("Y not integer!")
        continue
    if y >= 0:
        print("Y < 0!")
        continue
    print("Result (x ^ y): {}".format(minus(x, y)))
