#01년부터 22년까지 각각 최대일교차가 난 날짜와 일교차를 표시하시오
import weather
def temp_gap_year_idx(temp_gap, date, condition):
    date_idx = 0
    temp = 0
    for i in range(len(date)):
        year = date[i][0]
        if year in condition:
            if temp_gap[i] > temp:
                temp = temp_gap[i]
                date_idx = i
    return date_idx

def main():
    file = "hw/hw12/weather(146)_2001-2022.csv"
    tmax = weather.weather_float(file, 3)
    tmin = weather.weather_float(file, 5)
    dates = weather.dates(file)
    temp_gap = [tx - tn for tx, tn in zip(tmax, tmin)]

    for i in range(2001,2023):
        idx = temp_gap_year_idx(temp_gap, dates, [i])
        print(f'최대 일교차 날짜 {weather.date2str(dates[idx])} 최대 일교차 {temp_gap[idx]:.1f}')


if __name__ == "__main__":
    main()