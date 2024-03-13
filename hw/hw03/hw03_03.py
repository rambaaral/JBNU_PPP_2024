#hw02-3 수정하기
r=float(input("반지름을 입력해주세요.(cm)"))
import math
a=round(r**2*math.pi, 2)

print("반지름이 {}㎝인 원의 넓이는 약{}㎠입니다.".format(r, a))