from itertools import count, cycle

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
    try:
        start_number = int(input("Enter start number: "))
    except ValueError:
        print("Start number is not number!")
        continue
    string = input("Enter string fo repeate: ")
    
    print("first:")
    for i in count(start_number):
        if i >= start_number + cnt:
            break
        else:
            print(i)

    print("second:")
    for j in cycle(string):
        if cnt == 0:
            break
        else:
            print(string)
            cnt -= 1
