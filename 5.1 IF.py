cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print (car.upper ())
    else:
        print (car.title ())
#if 判断是区分大小写的
moto = 'Baojun'
if moto.lower() == 'BAojun'.lower() :
    print('true')
else:
    print('false')

# ！= 不相等判断
if moto != 'Bajun':
    print('不相等')
