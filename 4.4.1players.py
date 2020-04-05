'''
切片访问列表的元素

#注意 ，理解“切片”
[:3]和[-3:]  分别表示 前三个和倒数三个  包括3，而[2:]表示从2开始 不包含2个元素
当成‘切片’理解
'''

players = ['charles','martina','michael','florence','eli']
print(players[2:3])
#如果你没有指定第一个索引， Python将自动从列表开头开始：
print(players[:3])
#要让切片终止于列表末尾，也可使用类似的语法
print(players[2:])
#指定倒数三个数|
print(players[-1:])

#全部不指定
print(players[:])


# 遍历切片

print('Here are first three players on my team:')
for player in players[0:3]:
    print(player.title())