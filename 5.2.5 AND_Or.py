age_0 = 22
age_1 = 18
# and
if  age_0 >= 21 and age_1 >= 21 :
    print('true')
else:
    print('false')


# or
if  age_0 >= 21 or age_1 >= 21 :
    print('true')
else:
    print('false')

# in
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title()+',you can post a response if you wish.')

# 布尔判断

if (age_0 >= 21 or age_1 <= 21)==True:
    print('true')
else:
    print('false')
