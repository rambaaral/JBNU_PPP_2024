def total_calorie(fruits, fruits_calorie_dic):
    total = 0
    for item in fruits:
        total = total + fruits[item]*fruits_calorie_dic[item]/100
    return total

def main():
    fruits_calorie_dic = {"한라봉":50, "딸기":34, "바나나":77}
    fruits_mon = {"딸기":300, "한라봉":150}
    print(f"당신은 월요일에 {total_calorie(fruits_mon, fruits_calorie_dic):.2f}㎉를 먹었습니다.")

    fruits_wed = {"딸기":200, "바나나":300}
    print(f"당신은 수요일에 {total_calorie(fruits_wed, fruits_calorie_dic):.2f}㎉를 먹었습니다.")


if __name__ == "__main__":
    main()

#x for x in [list] 잘 활용하기
#return sum(gram*fruits_calorie_dic[name]/100 for name, gram in fruits.item())

#문자열을 숫자로 바꾸기
input_text = "1,2,3,4,5"
tokens = input_text.split(",")
result = []
for token in tokens:
    result.append(int(token))
print (result)