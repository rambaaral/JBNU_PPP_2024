def weather(filename, idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            tavg = float(tokens[idx])
            dataset.append(tavg)
    return dataset

def weather_int(filename, idx):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            tavg = int(tokens[idx])
            dataset.append(tavg)
    return dataset

# def long_rain(rlist):
#     rain_event = []

#     prev_rain_count = 0
#     for rain in rlist:
#         if rain == 0:
#             if prev_rain_count > 0:
#                 rain_event.append(prev_rain_count)
#             prev_rain_count = 0
#         else:
#             prev_rain_count += 1
#     return max(rain_event)

# def max_rain(rlist):
#     rain_event = []

#     prev_rain_count = 0
#     prev_rain = 0
#     for rain in rlist:
#         if rain == 0:
#             if prev_rain_count > 0:
#                 rain_event.append(prev_rain)
#             prev_rain_count = 0
#             prev_rain = 0
#         else:
#             prev_rain_count += 1
#             prev_rain += rain
#     return max(rain_event)

# # def trank(rlist, limit):
# #     return sorted(rlist)[:limit:-1]

# def sumifs(rainfall, months, condition):
#     total = 0
#     for i in range(len(rainfall)):
#         rain = rainfall[i]
#         month = months[i]
#         if month in condition:
#             total += rain
#     return total

def sumifs_year(rainfall, years, condition):
    total = 0
    for i in range(len(rainfall)):
        rain = rainfall[i]
        year = years[i]
        if year in condition:
            total += rain
    return total

def main():
    #weather_name = "week/w07/weather(146)_2022-2022.csv"
    weather_name2 = "hw/hw11/weather(146)_2001-2022.csv"
    rainfall = weather(weather_name2, 9)
    year = weather_int(weather_name2, 0)
    #tmax = weather(weather_name, 3)
    rainfall_2021 = sumifs_year(rainfall, year, [2021, 2022])
    print(f"{rainfall_2021}")



if __name__ == "__main__":
    main()