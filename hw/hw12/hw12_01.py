#01년부터 22년까지 각각 최대일교차가 난 날짜와 일교차를 표시하시오

def temp_gap_year_idx(temp_gap, years, condition):
    date_idx = 0
    temp = 0
    for i in range(len(years)):
        year = years[i]
        if year in condition:
            if temp_gap[i] > temp:
                temp = temp_gap[i]
                date_idx = i
    return date_idx

def main():
    import weather
    file = "hw/hw12/weather(146)_2001-2022.csv"
    tmax = weather.weather_float(file, 3)
    tmin = weather.weather_float(file, 5)
    year = weather.weather_int(file, 0)
    temp_gap = [tx - tn for tx, tn in zip(tmax, tmin)]

    for i in range(2001,2023):
        idx = temp_gap_year_idx(temp_gap, year, [i])
        print(f'{weather.dates(file)[idx]} {temp_gap[idx]:.1f}')


if __name__ == "__main__":
    main()