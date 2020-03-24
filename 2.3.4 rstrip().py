favorte_laguge = '   Py thon   '

# favorte_laguge=favorte_laguge.strip()   #要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中

print(favorte_laguge.strip()) # strip（）去除开头和末尾空格
print((favorte_laguge.rstrip()).lstrip()) # 和 strip()相等

print(favorte_laguge.lstrip())  # lstrip（）去除左空格
print((favorte_laguge.rstrip()).lstrip()) # rstrip（）去除又空格

Man_tall = 'Albert Einstein once said, “A person who never made a mistake never tried anythingnew.”'
print( Man_tall)