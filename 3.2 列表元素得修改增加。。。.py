"""
1.修改列表元素的语法与访问列表元素的语法类似
2.append（）给列表附加元素时，它将添加到列表末尾
3。方法insert()可在列表的任何位置添加新元素
4. 使用del语句删除元素
"""

motorcycle = ['honda','yamaha','suzuki']
print('原始',motorcycle)
#1.修改列表值
motorcycle [0] ='ducati'
print('修改',motorcycle)
#2.插入列表值
motorcycle.append('ducati')
print('增加',motorcycle)
#2.1空列添加元素、
motorcycle = []
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append("suzuki")
print('空增',motorcycle)

#3.insert（）
motorcycle.insert(2,'ducati')
print('索插',motorcycle)

#4. 使用del语句删除元素
del motorcycle[0]
print('删除',motorcycle)

