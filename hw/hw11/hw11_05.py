#21년과 22년 총 강수량은?

def weather(filename, idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            tavg = float(tokens[idx])
            dataset.append(tavg)
    return dataset

def weather_int(filename, idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            tavg = int(tokens[idx])
            dataset.append(tavg)
    return dataset

def sumifs_year(rainfall, years, condition):
    total = 0
    for i in range(len(rainfall)):
        rain = rainfall[i]
        year = years[i]
        if year in condition:
            total += rain
    return total

def main():
    weather_name = "hw/hw11/weather(146)_2001-2022.csv"
    rainfall = weather(weather_name, 9)
    year = weather_int(weather_name, 0)
    rainfall_2021 = sumifs_year(rainfall, year, [2021])
    rainfall_2022 = sumifs_year(rainfall, year, [2022])

    print(f"2021년의 총 강수량은 {rainfall_2021:.1f}ml이고 2022년의 총 강수량은 {rainfall_2022:.1f}ml입니다.")

if __name__ == "__main__":
    main()