'''
1、遍历元组 像列表一样，也可以使用for循环来遍历元组中的所有值
2.虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺
寸，可重新定义整个元组：
'''
#1，遍历元组

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

#2.修改元组变量

dimensions = (400,100)
print("\n Modified dimensions:")
for dimension in dimensions:
    print (dimension)
