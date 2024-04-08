#csv 파일을 사전형?으로 바꾸기
def text2list(a):
    tokens = a.split()
    result = []
    for token in tokens:
        result.append(int(token))
    return result

def read_cal_cb(filename):
    db = {}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            fruit_name = tokens[0]
            fruit_cal = int(tokens[1])
            db[fruit_name] = fruit_cal

    return db

def total_calorie(fruits, fruits_calorie_dic):
    total = 0
    for item in fruits:
        total = total + fruits[item]*fruits_calorie_dic[item]/100
    return total

def main():
    fruits_calorie_dic = read_cal_cb("week/w06/calorie_db.csv")
    fruits_mon = {"딸기":300}
    print(f"당신은 월요일에 {total_calorie(fruits_mon, fruits_calorie_dic):.2f}㎉를 먹었습니다.")

    fruits_wed = {"딸기":200, "바나나":300}
    print(f"당신은 수요일에 {total_calorie(fruits_wed, fruits_calorie_dic):.2f}㎉를 먹었습니다.")


if __name__ == "__main__":
    main()

