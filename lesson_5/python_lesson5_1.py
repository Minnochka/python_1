my_file = open("part_1.txt", "w", encoding="utf-8")
user = []
while True:
    d = input("Enter string: ")
    if d == "":
        break
    else:
        d +="\n"
    user.append(d)
my_file.writelines(user)
my_file.close()

