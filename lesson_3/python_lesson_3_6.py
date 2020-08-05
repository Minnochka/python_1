def str_title_f(old_str):
    new_str = []
    for n,i in enumerate(old_str):
        if (ord(i) >= 97 and ord(i) < 123) or ord(i) == 32:
            if n == 0 or (ord(old_str[n - 1]) == 32 and i != 32):
                new_str.append(i.upper())
            else:
                new_str.append(i)
        else:
            return "Error in string!"
    return "".join(new_str)

while True:
    my_str = input("Enter you string('end' for exit): ")
    if my_str == 'end':
        break
    print("Result: {}".format(str_title_f(my_str)))
    
