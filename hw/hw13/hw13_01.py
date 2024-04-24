#기상자료를 외부에서 받아서 전주의 연 평균 기온(일 평균 기온의 연 평균), 5mm이상 강우일수, 총 강우량
import weather
import requests

def rfd(rlist):
    total = 0
    for i in rlist:
        if i >= 5:
            total += 1
    return total


def main():
    URL = "https://api.taegon.kr/station/146/?sy=2020&ey=2020&format=csv"

    with open("hw/hw13/weather_146_2020.html","w",encoding="UTF-8-sig") as f:
        res = requests.get(URL)
        res.encoding = "UTF-8"
        f.write(res.text)

    file = "hw/hw13/weather_146_2020.html"
    tavg = weather.weather_float(file, 4)
    rf = weather.weather_float(file, 9)

    t_y_a = sum(tavg)/len(tavg)
    o_5mm_d = rfd(rf)
    sum_rf = sum(rf)

    filename = "hw/hw13/hw13_result.txt"

    with open (filename, "w", encoding="UTF-8") as fout:
        fout.write(f"2020년\n전주의 연 평균 기온은 {t_y_a:.2f}℃ 입니다.\n전주의 5mm이상 강우 일수는 {o_5mm_d}일 입니다.\n전주의 총 강우량은 {sum_rf:.2f}mm 입니다.")

if __name__ == "__main__":
    main()