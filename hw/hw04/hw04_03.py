#칼로리 계산 프로그램을 사전형을 이용하여 구현
eatf={"한라봉":0, "딸기":0, "바나나":0}
gpkca={"한라봉":0.50, "딸기":0.34, "바나나":0.77}

eatf["한라봉"]=float(input("섭취한 한라봉의 무게를 입력해주세요.(g)"))
eatf["딸기"]=float(input("섭취한 딸기의 무게를 입력해주세요.(g)"))
eatf["바나나"]=float(input("섭취한 바나나의 무게를 입력해주세요.(g)"))

kca=eatf["한라봉"]*gpkca["한라봉"]+eatf["딸기"]*gpkca["딸기"]+eatf["바나나"]*gpkca["바나나"]


print("당신은 방금 {:0.2f}㎉섭취했습니다.".format(kca))