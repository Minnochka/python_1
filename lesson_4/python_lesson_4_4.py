import random

while True:
    cnt = input("Enter count of random numbers ('end for exit): ")
    if not cnt.isdigit():
        if cnt == 'end':
            break
        else:
            print("Count is not number!")
            continue
    else:
        cnt = int(cnt)
    try:
        start_number = int(input("Enter start number: "))
    except ValueError:
        print("Start number is not number!")
        continue
    try:
        end_number = int(input("Enter end number: "))
    except ValueError:
        print("End number is not number!")
        continue
    
    l = [random.randint(start_number, end_number) for el in range(0, cnt)]
    r = [el for el in l if l.count(el) == 1]
    print(l)
    print(r)
