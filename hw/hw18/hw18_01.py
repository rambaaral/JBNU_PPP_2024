#그래프
import matplotlib.pyplot as plt
import os

def callfile(filestation,URL):
    import requests
    with open(filestation,"w",encoding="UTF-8-sig") as f:
        res = requests.get(URL)
        res.encoding = "UTF-8"
        f.write(res.text.replace("\r", ""))

def weather_list(filename, idxlen):
    dataset = []
    with open(filename, encoding="utf-8-sig") as f:

        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split(",")
            if len(tokens)-1 >= idxlen:
                if not '' in tokens:
                    dataset.append(tokens)
    return dataset

def weather_float(list, idx, aaa):
    dataset = []
    for i in range(len(list)):
        if i != 0:
            if i in aaa:
                dataset.append(float(list[i][idx]))
    return dataset

def weather_int(list, idx, aaa):
    dataset = []
    for i in range(len(list)):
        if i != 0:
            if i in aaa:
                dataset.append(int(list[i][idx]))
    return dataset

def weather_year(list, idx, aaa):
    dataset = []
    for i in range(len(list)):
        if i != 0:
            if i in aaa:
                tokens = str(list[i][idx]).split("-")
                dataset.append(tokens[0])
    return dataset

def weather_str(list, idx, name=True):
    dataset = []
    if name == True:
        for i in range(len(list)):
            if i != 0:
                dataset.append(str(list[i][idx]))
    else:
        for i in range(len(list)):
            dataset.append(str(list[i][idx]))
    return dataset

def main():
    url = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    file = "hw/hw18/wlist.csv"
    if not os.path.exists("wlist.csv"):
        callfile(file,url)
    
    weatherlist = weather_list(file, 4)

    dates = weather_str(weatherlist, 0)

    Bday_idx = []
    for i in range(len(dates)):
        tokens = dates[i].split("-")
        if int(tokens[0]) >= 1980 and int(tokens[0]) <= 2023:
            if int(tokens[1]) == 2 and int(tokens[2]) == 7:
                Bday_idx.append(i)

    winter_idx = []
    for i in range(len(dates)):
        tokens = dates[i].split("-")
        if int(tokens[0]) >= 1980 and int(tokens[0]) <= 2023:
            if int(tokens[1]) in [12, 1, 2]:
                winter_idx.append(i)

    summer_idx = []
    for i in range(len(dates)):
        tokens = dates[i].split("-")
        if int(tokens[0]) >= 1980 and int(tokens[0]) <= 2023:
            if int(tokens[1]) in [6, 7, 8]:
                summer_idx.append(i)


    plt.rcParams['font.family'] = 'Malgun Gothic'

    """
    Bday_tmax = weather_float(weatherlist, 4, Bday_idx)
    Bday_tmin = weather_float(weatherlist, 3, Bday_idx)
    Bday_date = weather_year(weatherlist, 0, Bday_idx)

    plt.plot(Bday_date, Bday_tmax, color="r", label ="최고기온")
    plt.plot(Bday_date, Bday_tmin, color="b", label ="최저기온")

    plt.title("내 생일 기온")
    plt.ylabel("섭씨온도")
    plt.xlabel("년도")
    """
    """
    winter_tmean = weather_float(weatherlist, 3, winter_idx)
    winter_date = weather_year(weatherlist, 0, winter_idx)

    plt.scatter(winter_date, winter_tmean)

    plt.title("년도별 겨울철 온도분포(일평균)")
    plt.ylabel("섭씨온도")
    plt.xlabel("년도")
    """
    """
    summer_tmean = weather_float(weatherlist, 3, summer_idx)
    summer_date = weather_year(weatherlist, 0, summer_idx)

    plt.scatter(summer_date, summer_tmean)

    plt.title("년도별 여름철 온도분포(일평균)")
    plt.ylabel("섭씨온도")
    plt.xlabel("년도")
    """

    plt.grid(True)

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()