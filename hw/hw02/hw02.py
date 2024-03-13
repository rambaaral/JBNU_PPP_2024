
cd1 = 30
cd2 = 0
fd1 = round((cd1*1.8) + 32, 2)
fd2 = round((cd2*1.8) + 32, 2)
print("섭씨 {}도는 화씨 {}도 입니다.".format(cd1, fd1))
print("섭씨 {}도는 화씨 {}도 입니다.".format(cd2, fd2))

weight = 60
height = 170
BMI = round(weight/(height/100)**2, 2)
print("몸무게가 {}kg, 키가 {}cm인 사람의 BMI수치는 {}입니다.".format(weight, height, BMI))

r = 4
c = round(r*r*3.141592, 2)
print("반지름이 {}인 원의 넓이는 {}입니다.".format(r, c))

a = 5
b = 3
h = 4
s = (a + b)/2*h
print("밑변이 {}, 윗변이 {}, 높이가 {}인 사다리꼴의 넓이는 {}입니다.".format(a, b, h, s))
