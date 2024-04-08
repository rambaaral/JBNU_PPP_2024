#csv파일을 불러와서 사전형으로 만들고 칼로리 계산 프로그램 만들기
def read_name_db(filename):
    db = {}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            fruit_name = tokens[0]
            db[fruit_name] = 0

    return db

def read_cal_db(filename):
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
    fruits = read_name_db("hw/hw10/calorie_db.csv")
    fruits_calorie_dic = read_cal_db("hw/hw10/calorie_db.csv")
    while True:
        fru = input("먹은 작물을 입력해주세요.(전부 입력했으면 '없음' 입력)")
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