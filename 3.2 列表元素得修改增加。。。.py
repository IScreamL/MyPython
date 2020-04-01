"""
1.修改列表元素的语法与访问列表元素的语法类似
2.append（）给列表附加元素时，它将添加到列表末尾
3。方法insert()可在列表的任何位置添加新元素
4. 使用del语句删除元素
5. 使用pop()来删除列表中任何位置的元素，只需在括号中指定要删除的元素
的索引即可，并让你能够接着使用它，默认删除列表末尾的元素。
6.区分 del 或者 pop()
如果你不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：如果你要从列表
中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续
使用它，就使用方法pop()。
7. remove() 从列表中删除元素时，也可接着使用它的值 ，注意方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，
就需要使用循环来判断是否删除了所有这样的值。
"""

motorcycle = ['honda', 'yamaha', 'suzuki']
print('原始', motorcycle)
# 1.修改列表值
motorcycle[0] = 'ducati'
print('修改', motorcycle)
# 2.插入列表值
motorcycle.append('ducati')
print('增加', motorcycle)
# 2.1空列添加元素、
motorcycle = []
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append("suzuki")
print('空增', motorcycle)

# 3.insert（）
motorcycle.insert(2, 'ducati')
print('索插', motorcycle)

# 4. 使用del语句删除元素
del motorcycle[0]
print('删除', motorcycle)

# 5 pop()
print(motorcycle)
pop_mot = motorcycle.pop(1)
print(motorcycle)
print('pop删除', pop_mot)

# 7.remove()
print(motorcycle)
to_remove = 'yamaha'
motorcycle.remove(to_remove)
print('7.指定值删除',motorcycle)

input('请输入值：')