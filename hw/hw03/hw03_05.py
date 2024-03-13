#칼로리 구하기
ore=float(input("섭취한 한라봉의 무게를 입력해주세요.(g)"))
str=float(input("섭취한 딸기의 무게를 입력해주세요.(g)"))
ban=float(input("섭취한 바나나의 무게를 입력해주세요.(g)"))
kca=round((ore*50/100)+(str*34/100)+(ban*77/100), 2)

print("당신은 방금 {}㎉섭취했습니다.".format(kca))