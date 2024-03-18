#BMI 수치 비만 정도 표시
w=float(input("몸무게를 입력해주세요.(kg)"))
h=float(input("키를 입력해주세요.(cm)"))
import math
bmi=round(w/math.pow(h/100, 2), 2)

print("몸무게가 {}kg, 키가 {}cm인 사람의 BMI수치는 {}입니다.".format(w, h, bmi))

if bmi < 23:
    print("비만이 아닙니다.")
elif bmi < 25:
    print("비만 전단계 입니다.")
elif bmi < 30:
    print("1단계 비만입니다.")
elif bmi < 35:
    print("2단계 비만입니다.")
else:
    print("3단계 비만입니다.")