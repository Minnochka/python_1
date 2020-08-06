from functools import reduce


#l = [el for el in range(100, 1001) if el % 2 == 0]
#res = reduce(lambda x,y: x * y, l)
#print (res)

print(reduce(lambda x,y: x * y, [el for el in range(100, 1001) if el % 2 == 0]))
