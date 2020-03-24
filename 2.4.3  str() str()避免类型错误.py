'''
函数str()显式 地指出你希望Python将这个整数用作字符串
'''

age = 23
# message = ' Happy' + age + ' ** Birthda'
message = ' Happy\t' + str(age) + ' ** Birthda'

print(message)


'''
在Python 2计算整数结果时，采取的方式不是四舍五入，而是将小数部分直接删除
Python3 不会

'''

a = 3/2
b = 3.0/2
c = 3/2.0
d = 3.0/2.0

print(a,b,c,d)

