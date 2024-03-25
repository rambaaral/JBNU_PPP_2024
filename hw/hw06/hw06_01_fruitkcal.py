#반복문, 사전 활용한 칼로리 계산
eatf={"한라봉":0, "딸기":0, "바나나":0}
fgram={"한라봉":0, "딸기":0, "바나나":0}
kcalpg={"한라봉":0.50, "딸기":0.34, "바나나":0.77}
stomach = []

def auto(fruit):
    fgram[f"{fruit}"]=float(input(f"{fruit} 한개의 무게를 입력해주세요.(g)"))
    if fgram[f"{fruit}"] < 0:
        print("유효하지 않은 숫자입니다. 처음부터 다시 입력해주세요")
        auto(fruit)

    eatf[f"{fruit}"]=int(input(f"먹은 {fruit}의 개수를 입력해주세요"))
    if fgram[f"{fruit}"] < 0:
        print("유효하지 않은 숫자입니다. 처음부터 다시 입력해주세요")
        auto(fruit)
        
    i = 0
    while i < eatf[f"{fruit}"]:
        stomach.append(f"{fruit}")
        i += 1

def main():
    auto("한라봉")

    auto("딸기")

    auto("바나나")

    kcal = 0
    for item in stomach:
        kcal += fgram[item]*kcalpg[item]

    print(f"당신은 방금 {kcal:0.2f}㎉섭취했습니다.")

if __name__ == "__main__":
    main()