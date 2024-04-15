#가장 더운날 top3
def weather(filename, idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            tavg = float(tokens[idx])
            dataset.append(tavg)
    return dataset

def trank(wlist, limit):
    return sorted(wlist, reverse=True)[:limit]

def main():
    weather_name = "hw/hw11/weather(146)_2022-2022.csv"
    tmax = weather(weather_name, 3)
    print(f"가장 더운 날 top3의 온도(섭씨)는 {trank(tmax, 3)}입니다.")

if __name__ == "__main__":
    main()