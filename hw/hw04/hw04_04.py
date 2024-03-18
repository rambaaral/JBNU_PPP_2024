#원의 둘레와 면적을 출력하는 프로그램 작성 둘레는 소수점 한자리 면적은 두자리 라운드 함수 말고 출력시 포맷 기능 사용
r=float(input("반지름을 입력해주세요.(cm)"))
import math

l=2*r*math.pi
a=math.pow(r, 2)*math.pi

print("반지름이 {:0.2f}㎝인 원의 둘래의 길이는 약 {:0.1f}㎝, 넓이는 약{:0.2f}㎠입니다.".format(r, l, a))