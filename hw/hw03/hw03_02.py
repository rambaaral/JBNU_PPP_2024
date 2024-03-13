#실습 2, 3 완성
w=float(input("몸무게를 입력해주세요.(kg)"))
h=float(input("키를 입력해주세요.(cm)"))
bmi=round(w/(h/100)**2, 2)

print("몸무게가 {}kg, 키가 {}cm인 사람의 BMI수치는 {}입니다.".format(w, h, bmi))
