"""
1.for  in 遍历列表
2.在for循环后面，没有缩进的代码都只执行一次，而不会重复执行。


"""
# 4.1  for in遍历显示
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(magician.title() + ', that was a great trick!'+'.\n')
print("Thank you , everyone . That was a great magic show!")
