"""
1.sort()按与字母顺序相反的顺序排列列表元素,参数reverse=True反序
  永久性地修改了列表元素的排列顺序
2. sorted()对列表进行临时排序
3.reverse()永久反转列表排序，注意， reverse()不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排
列顺序：
4.len（）确认列表的长度


"""

#1.sort()
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# 2.sorted()
cars2 = ['bmw','audi','toyota','subaru']
print('元素值',cars2)
print('排序值',sorted(cars2))
print('sorted排序后的值',cars2)
cars2.sort()
print('sort排序后原始值',cars2)

# 3.reverse()
cars3 = ['bwm','audo','toyouta','subaru']
cars3.reverse()
print('reverse相反排列',cars3)

#4 len()
cars4 = ['bwm','audo','toyouta','subaru']
print(len(cars4))