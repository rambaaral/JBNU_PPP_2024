#01년부터 22년까지 각 해마다 5월부터 9월까지 적산온도를 구하시오
import weather
def ggd_temp_year(tavg, date, condition):
    ggd_temp = 0
    for i in range(len(date)):
        year = date[i][0]
        month = date[i][1]
        if year in condition and month in [5, 6, 7, 8, 9]:
            if tavg[i] - 5 > 0:
                ggd_temp += (tavg[i]-5)
            else:
                pass
    return ggd_temp


def ggd_temp_year(tavg, dates, condition):
    ggd_temp = 0
    for i in range(len(dates)):
        year = dates[i][0]
        month = dates[i][1]
        if year in condition and month in [5, 6, 7, 8, 9]:
            if tavg[i] - 5 > 0:
                ggd_temp += (tavg[i]-5)
            else:
                pass
    return ggd_temp

def main():
    file = "hw/hw12/weather(146)_2001-2022.csv"
    tavg = weather.weather_float(file, 4)
    dates = weather.dates(file)

    for i in range(2001,2023):
        ggd_temp = ggd_temp_year(tavg, dates, [i])
        print(f'{i}년 적산온도 {ggd_temp:.1f}')


if __name__ == "__main__":
    main()