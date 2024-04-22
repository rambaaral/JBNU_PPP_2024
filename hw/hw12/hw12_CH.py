#01년부터 22년까지 각 해마다 4월부터 시작해서 적산온도가 200이 넘는 최초일을 구하시오
import weather
def first_ggd_temp_year(tavg, date, condition):
    idx = None
    ggd_temp = 0
    for i in range(len(date)):
        year = date[i][0]
        month = date[i][1]
        if year in condition and month in range(4,12):
            if tavg[i] - 5 > 0:
                ggd_temp += (tavg[i]-5)
                if ggd_temp > 200:
                    idx = i
                    return idx
    return idx

def main():
    file = "hw/hw12/weather(146)_2001-2022.csv"
    tavg = weather.weather_float(file, 4)
    dates = weather.dates(file)

    for i in range(2001,2023):
        idx = first_ggd_temp_year(tavg, dates, [i])
        print(f'{i}년에 적산온도가 200을 넘는 최초일 {weather.date2str(dates[idx])}')


if __name__ == "__main__":
    main()