#기상자료를 받아서 전주의 연 평균 기온(일 평균 기온의 연 평균), 5mm이상 강우일수, 총 강우량
def read_wea_db_tavg(filename):
    db = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            tavg = float(tokens[4])
            db.append(tavg)
    
    return sum(db)/len(db)

def read_wea_db_rf(filename):
    db = 0
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            rf = float(tokens[9])
            if rf >= 5:
                db += 1

    return db

def read_wea_db_srf(filename):
    db = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            srf = float(tokens[9])
            db.append(srf)
    
    return sum(db)

def main():
    t_y_a = read_wea_db_tavg("hw/hw10/weather(146)_2022-2022.csv")
    o_5mm_d = read_wea_db_rf("hw/hw10/weather(146)_2022-2022.csv")
    sum_rf = read_wea_db_srf("hw/hw10/weather(146)_2022-2022.csv")
    print(f"전주의 연 평균 기온은 {t_y_a:.2f}℃ 입니다.")
    print(f"전주의 5mm이상 강우 일수는 {o_5mm_d}일 입니다.")
    print(f"전체의 총 강우량은 {sum_rf:.2f}mm 입니다.")

if __name__ == "__main__":
    main()