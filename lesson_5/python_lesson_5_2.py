try:
    with open("part_2.txt", "r", encoding = "utf-8") as my_file:
        strs = my_file.read().splitlines()
    print("Count of strings: {}".format(len(strs)))
    for i, s in enumerate(strs):
        print("Count of words (String {}): {}".format(i + 1, len(s.split())))
except FileNotFoundError:
    print("File not found! Please, create file.")
