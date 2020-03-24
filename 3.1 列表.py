"""
1.列表由一系列按特定顺序排列的元素组成。
2.列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。
要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。
3.通过将索引指定为-1，可访问最后一个列表元素（注意-1表示最后索引，反之-2表示倒数第二个。。。）
"""
bicycles = ['trek', 'cannnandale', 'redline', 'specializde']
print(bicycles)
print(bicycles[2],bicycles[0],bicycles[-1],bicycles[3].title(),bicycles[-2])
print('My first bicycle was a ' +bicycles[2].title()+'.')


