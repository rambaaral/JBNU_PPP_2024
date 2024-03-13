#hw02.4 수정하기
up=float(input("사다리꼴의 윗변의 길이를 입력해주세요.(cm)"))
do=float(input("사다리꼴의 밑변의 길이를 입력해주세요.(cm)"))
he=float(input("사다리꼴의 높이를 입력해주세요.(cm)"))
a=round(((up+do)/2)*he, 2)

print("윗변의 길이가 {}㎝, 밑변의 길이가 {}㎝, 높이가 {}㎝인 사다리꼴의 넓이는 {}㎠입니다.".format(up, do, he, a))