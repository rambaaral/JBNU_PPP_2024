#반복문과 사전형을 이용하여 칼로리 계산
eatf={"한라봉":0, "딸기":0, "바나나":0}
fgram={"한라봉":0, "딸기":0, "바나나":0}
kcalpg={"한라봉":0.50, "딸기":0.34, "바나나":0.77}
stomach = []

def auto(fruit):
    fgram[f"{fruit}"]=float(input(f"{fruit} 한개의 무게를 입력해주세요.(g)"))
    eatf[f"{fruit}"]=float(input(f"먹은 {fruit}의 개수를 입력해주세요"))
    for i in range(int(eatf[f"{fruit}"])):
        stomach.append(f"{fruit}")
        i = i + 1

auto("한라봉")

auto("딸기")

auto("바나나")

kcal = 0
for item in stomach:
    kcal += fgram[item]*kcalpg[item]

print(f"당신은 방금 {kcal:0.2f}㎉섭취했습니다.")