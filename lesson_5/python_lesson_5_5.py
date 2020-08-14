import random

l = []
while len(l) == 0:
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
print(l)
my_file = open("nums.txt", "w+", encoding="utf-8")
my_file.write(' '.join(str(e) for e in l))
my_file.seek(0)
sum_i = 0
for i in my_file.readline().split():
    sum_i += int(i)
print("Сумма: " + str(sum_i))
my_file.close()

    
