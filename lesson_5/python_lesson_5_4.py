words_en = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
words_rus = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
try:
    with open("file_en.txt", "r", encoding="utf-8") as my_file:
        strs = my_file.readlines()
        #print(strs)
    rus_f = open("file_rus.txt", "w", encoding="utf-8")
    for e in strs:
        words = e.partition(' ')
        #print(words)
        for w_en, w_rus in zip(words_en, words_rus):
            if w_en == words[0].lower():
                rus_f.write(w_rus + ''.join(e for e in words[1:]))
    rus_f.close()
except FileNotFoundError:
    print("File not found! Please, create file.")
