'''
1.range()让你能够轻松地生成一系列的数字
2.使用 range()创建数字列表(函数list()将range()的结果直接转换为列表)
3.list()指定步长
4.range()几乎能够创建任何需要的数字集，例如，如何创建一个列表，其中包含前
  10个整数（即1~10）的平方呢？在Python中，两个星号（ **）表示乘方运算

5.统计数列的 最大值，最小值，和。。
'''
#1

for value in range(1,5):
    print(value)

#2
number = list(range(1,5))
print(number)
#3
numbers = list(range(2,10,2))
print(numbers)

#4
squares = []
for nums in range(1,10):
    square=nums**2
    squares.append(square)

print(squares)

squares2 = []
for nums2 in range(1, 10):
    squares2.append(nums2**2)

    print(squares2)


#5
digits = list(range(1,5))
print('min',min(digits),'\nmax:',max(digits)
      ,'\nsum:', sum(digits))