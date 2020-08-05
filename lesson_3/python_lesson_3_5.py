def sum_f(list_el):
    new_list = []
    for i, num in enumerate(my_list):
        try:
            new_list.append(float(num))
        except ValueError:
            return(1, sum(new_list))
    return (0, sum(new_list))
    

sum_all = 0
while True:
    my_list = input("Enter numbers(Another symbol for exit): ").split()
    res = sum_f(my_list)
    sum_all += res[1]
    print("Result: {}".format(sum_all))
    if res[0] == 1:
        break
            
