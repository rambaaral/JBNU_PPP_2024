#강우이벤트 중 최대 강수량은? 비가 연속으로 올 떄, 하나의 강우 이벤트로 가정
def weather(filename, idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            tavg = float(tokens[idx])
            dataset.append(tavg)
    return dataset

def max_rain(wlist):
    rain_event = []

    prev_rain_count = 0
    prev_rain = 0
    for rain in wlist:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain)
            prev_rain_count = 0
            prev_rain = 0
        else:
            prev_rain_count += 1
            prev_rain += rain
    return max(rain_event)

def main():
    weather_name = "hw/hw11/weather(146)_2022-2022.csv"
    rainfall = weather(weather_name, 9)
    print(f"최대 강수량은 {max_rain(rainfall):.1f}ml입니다.")



if __name__ == "__main__":
    main()