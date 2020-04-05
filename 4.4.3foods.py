'''
注意使用切片来复制
friend_foods = my_foos[:]
friend_foods1 = my_foos1
'''
#1
my_foos = ['pizza','falafel','carrot cake']
friend_foods = my_foos[:]


my_foos.append('canoli')
friend_foods.append('ice cream')

print('my_foods',my_foos)
print('friend',friend_foods)

#2
my_foos1 = ['pizza','falafel','carrot cake']
friend_foods1 = my_foos1

my_foos1.append('canoli')
friend_foods1.append('ice cream')

print('my_foods',my_foos1)
print('friend',friend_foods1)
