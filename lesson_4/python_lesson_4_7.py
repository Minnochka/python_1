import math

def fact_f(cnt):
    for i in range(1,cnt + 1):
        yield math.factorial(i)

while True:
    cnt = input("Enter count of numbers ('end' for exit): ")
    if not cnt.isdigit():
        if cnt == 'end':
            break
        else:
            print("Count is not number!")
            continue
    else:
        cnt = int(cnt)
        
    for i, r in enumerate(fact_f(cnt)):
        print("{}! = {}".format(i + 1, str(r)))
