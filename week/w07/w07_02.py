
def weather_float(filename, idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            token = float(tokens[idx])
            dataset.append(token)
    return dataset

def weather_int(filename, idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            token = int(tokens[idx])
            dataset.append(token)
    return dataset

def dates(filename):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            years = int(tokens[0])
            months = int(tokens[1])
            days = int(tokens[2])
            dataset.append([years, months, days])
    return dataset

def gdd_season(tavg, months):
    # total_gdd = 0
    # for temp, month in zip(tavg, months):
    #     if month in [5, 6, 7, 8, 9]:
    #         eff_temp = temp-5
    #         if eff_temp < 0:
    #             eff_temp = 0
    #         total_gdd += eff_temp
    # return total_gdd
    total_gdd = sum([temp - 5 if temp -5 > 0 else 0 for temp, month in zip(tavg, months) if month in [5, 6, 7, 8, 9]])
    return total_gdd

def main():
    file = "week/w07/weather(146)_2022-2022.csv"
    tmax = weather_float(file, 3)
    tmin = weather_float(file, 5)
    month = weather_int(file, 1)
    tavg = weather_float(file, 4)
    date = dates(file)

    # temp_gap = []
    # for i in range(len(tmax)):
    #     temp_gap.append(tmax[i]-tmin[i])
    # for tx, tn in zip(tmax, tmin):
    #     temp_gap.append(tx - tn)
    temp_gap = [tx-tn for tx, tn in zip(tmax, tmin)]

    # max_idx = 0
    # max_diff_temp = 0
    # i = 0
    # for td in temp_gap:
    #     if max_diff_temp < td:
    #         max_diff_temp = td
    #         max_idx = i
    #     i += 1
    max_idx = temp_gap.index(max(temp_gap))

    print(f'일교차가 가장 큰 날은 {date[max_idx]}이고 최대 일교차는 {max(temp_gap):.1f}입니다.')
    
    print(f'{gdd_season(tavg, month)}')
    
if __name__ == "__main__":
    main()