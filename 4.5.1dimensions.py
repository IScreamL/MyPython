'''
1.Python将不能修改的值称为不可变的，而不可变的列表被称为元组。

'''
#1
dimensions = (200,5)
print(dimensions[0])
print(dimensions[1])

#2尝试修改元组  tip:元组对象不支持项分配

dimensions [1]=30