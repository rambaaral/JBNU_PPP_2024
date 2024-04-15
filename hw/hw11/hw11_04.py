#여름철(6월-8월) 총 강수량은? sumifs(rainfall, month, selected=[6,7,8])
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

def sumifs(rainfall, months, condition):
    total = 0
    for i in range(len(rainfall)):
        rain = rainfall[i]
        month = months[i]
        if month in condition:
            total += rain
    return total

def main():
    weather_name = "hw/hw11/weather(146)_2022-2022.csv"
    rainfall = weather(weather_name, 9)
    month = weather_int(weather_name, 1)
    print(f"여름철 총 강수량은 {sumifs(rainfall, month, [6, 7, 8]):.1f}ml입니다.")

if __name__ == "__main__":
    main()