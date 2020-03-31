"""
1.sort()按与字母顺序相反的顺序排列列表元素,参数reverse=True反序
  永久性地修改了列表元素的排列顺序
2. sorted()对列表进行临时排序
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

