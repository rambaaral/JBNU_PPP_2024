#관측이래 전주에서 최고온도와 그 날짜, 그리고 가장 큰 일교차와 해당 일자를 구하시오.
#날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)
"""
csv 파일을 불러온 후 필요한 자료들은 list 형태로 만들었습니다.              예)[[날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)],...]
list 형태로 만들 때 값이 하나라도 존재하지 않는 날은 포함하지 않았습니다.    예)최고기온 값만 존재하는 1918년8월7일
"""
import weather
import hw_submission

def main():
    url = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filestaion = "hw/hw14/wlist.csv"
    weather.callfile(filestaion,url)
    weather_list = weather.weather_list(filestaion, 4)
    tmax = weather.weather_float(weather_list, 4)
    tmin = weather.weather_float(weather_list, 3)
    date = weather.weather_str(weather_list, 0)
    tmax_idx = tmax.index(max(tmax))
    gapmax = [tx-tn for tx, tn in zip(tmax, tmin)]
    gapmax_idx = gapmax.index(max(gapmax))

    hw_submission.submit("김성은", max(tmax), date[tmax_idx], max(gapmax), date[gapmax_idx])

if __name__ == "__main__":
    main()