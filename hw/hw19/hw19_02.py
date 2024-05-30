#자유과제
#tkinter, matplotlib 조합
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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




def plot_graph(graph_type):
    fig.clear()
    ax = fig.add_subplot(111)
    
    if graph_type == 'birthday':
        Bday_tmax = weather_float(weatherlist, 4, Bday_idx)
        Bday_tmin = weather_float(weatherlist, 3, Bday_idx)
        Bday_date = weather_year(weatherlist, 0, Bday_idx)
        x = Bday_date
        y1 = Bday_tmax
        y2 = Bday_tmin
        ax.plot(x, y1)
        ax.plot(x, y2)
        ax.set_title('년도별 생일 온도분포')
    elif graph_type == 'summer':
        summer_tmean = weather_float(weatherlist, 3, summer_idx)
        summer_date = weather_year(weatherlist, 0, summer_idx)
        x = summer_date
        y = summer_tmean
        ax.scatter(x, y)
        ax.set_title('년도별 여름철 온도분포(평균)')
    elif graph_type == 'winter':
        winter_tmean = weather_float(weatherlist, 3, winter_idx)
        winter_date = weather_year(weatherlist, 0, winter_idx)
        x = winter_date
        y = winter_tmean
        ax.scatter(x, y)
        ax.set_title('년도별 겨울철 온도분포(평균)')
        
    ax.grid(True)
    canvas.draw()

def main():
    global canvas, fig, weatherlist, Bday_idx, summer_idx, winter_idx

    url = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    file = "hw/hw19/wlist.csv"
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

    summer_idx = []
    for i in range(len(dates)):
        tokens = dates[i].split("-")
        if int(tokens[0]) >= 1980 and int(tokens[0]) <= 2023:
            if int(tokens[1]) in [6, 7, 8]:
                summer_idx.append(i)

    winter_idx = []
    for i in range(len(dates)):
        tokens = dates[i].split("-")
        if int(tokens[0]) >= 1980 and int(tokens[0]) <= 2023:
            if int(tokens[1]) in [12, 1, 2]:
                winter_idx.append(i)


    plt.rcParams['font.family'] = 'Malgun Gothic'

    window = tk.Tk()
    window.title("1980-2023 주제별 온도 그래프")


    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)


    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    btn_line = tk.Button(window, text="생일 온도", command=lambda: plot_graph('birthday'))
    btn_line.pack(side=tk.LEFT)

    btn_scatter = tk.Button(window, text="여름철 온도", command=lambda: plot_graph('summer'))
    btn_scatter.pack(side=tk.LEFT)

    btn_bar = tk.Button(window, text="겨울철 온도", command=lambda: plot_graph('winter'))
    btn_bar.pack(side=tk.LEFT)


    window.mainloop()

if __name__ == "__main__":
    main()
