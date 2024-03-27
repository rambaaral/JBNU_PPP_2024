#딸기 300 한라봉 150을 섭취했을 때 입력자료를 사전형으로 전달하면 총 칼로리를 계산하는 함수 만들기
#함수는 total_calorie(fruits, fruits_calorie_dic)
#fruits={"딸기":300, "한라봉":150}
#fruits_calorie_dic={"한라봉":50, "딸기":34, "바나나":77}
def total_calorie(fruits, fruits_calorie_dic):
    total = 0
    for item in fruits:
        total = total + fruits[item]*fruits_calorie_dic[item]/100
    return total

def main():
    fruits = {"딸기":0, "한라봉":0, "바나나":0}
    fruits_calorie_dic = {"한라봉":50, "딸기":34, "바나나":77}
    while True:
        fru = input("먹은 과일을 입력해주세요.(전부 입력했으면 '없음' 입력)")
        if fru in fruits:
            fruits[fru] = fruits[fru] + float(input("먹은 무게를 입력해주세요.(g)"))
        elif fru == "없음":
            break
        else:
            print("유효하지 않은 접근입니다.")
    
    res = total_calorie(fruits, fruits_calorie_dic)
    print(f"당신은 방금 {res:.2f}㎉를 먹었습니다.")


if __name__ == "__main__":
    main()

