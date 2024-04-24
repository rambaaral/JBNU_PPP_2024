#파일입력
#지금 이것도 진도가 빠른 편이 아니라는 교수님의 발언 아으앗
#다음 부터는 매주 주제가 바뀔거다
#돌려쓰기 못한다?
#오늘은 인터넷에서 파일 긁어오기

def main():


    import os
    import requests

    url = "https://coopjbnu.kr/function/ajax.get.rest.data.php"
    urL = "https://api.taegon.kr/station/146/?sy=2022&ey=2022&format=csv"

    data = {"code":"mobile1"}

    with open("./cafeteria_menu.html","w",encoding="UTF-8") as f:
        res = requests.post(url, data=data)
        res.encoding = "UTF-8"
        f.write(res.text)

    if not os.path.exists("weather_146_2022.html"): #파일이 있는지 확인
        with open("./weather_146_2022.html","w",encoding="UTF-8-sig") as f:
            res = requests.get(urL)
            res.encoding = "UTF-8"
            f.write(res.text)

    # filename = "week/w08/yeze.txt"

    # with open (filename, "w") as fout:
    #     fout.write("Hello, World!")

if __name__ == "__main__":
    main()