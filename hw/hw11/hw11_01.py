#최장연속강우일수구하기
def long_rain(wlist):
    rain_event = []

    prev_rain_count = 0
    for rain in wlist:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain_count)
            prev_rain_count = 0
        else:
            prev_rain_count += 1
    return max(rain_event)

def main():
    import weather
    weather_name = "hw/hw11/weather(146)_2022-2022.csv"
    rainfall = weather.weather_float(weather_name, 9)
    print(f"최장연속강우일수는 {long_rain(rainfall)}일 입니다.")

if __name__ == "__main__":
    main()