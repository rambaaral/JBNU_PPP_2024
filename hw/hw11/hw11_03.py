#가장 더운날 top3
def trank(wlist, limit):
    return sorted(wlist, reverse=True)[:limit]

def main():
    import weather
    weather_name = "hw/hw11/weather(146)_2022-2022.csv"
    tmax = weather.weather_float(weather_name, 3)
    print(f"가장 더운 날 top3의 온도(섭씨)는 {trank(tmax, 3)}입니다.")

if __name__ == "__main__":
    main()