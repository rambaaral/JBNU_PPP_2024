#01년부터 22년까지 각 해마다 4월부터 시작해서 적산온도가 200이 넘는 최초일을 구하시오
def first_ggd_temp_year(tavg, years, months, condition):
    idx = 0
    ggd_temp = 0
    for i in range(len(years)):
        year = years[i]
        month = months[i]
        if year in condition and month in range(4,12):
            if tavg[i] - 5 > 0:
                ggd_temp += (tavg[i]-5)
                if ggd_temp > 200:
                    idx = i
                    break
    return idx

def main():
    import weather
    file = "hw/hw12/weather(146)_2001-2022.csv"
    tavg = weather.weather_float(file, 4)
    year = weather.weather_int(file, 0)
    month = weather.weather_int(file, 1)

    for i in range(2001,2023):
        idx = first_ggd_temp_year(tavg, year, month, [i])
        print(f'{i}년에 적산온도가 200을 넘는 최초일 {weather.dates(file)[idx]}')


if __name__ == "__main__":
    main()