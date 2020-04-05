'''
for循环为for value in range(1,11)，它将值1~10提供给表达式value**2。请注意，这里的for
语句末尾没有冒号。
'''

squares = [valus**2 for valus in range(1,10)]
print('列表简析',squares)

