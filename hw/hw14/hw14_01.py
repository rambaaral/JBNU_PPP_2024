#관측이래 전주에서 최고온도와 그 날짜, 그리고 가장 큰 일교차와 해당 일자를 구하시오.
#날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)
"""
날짜가 존재하는 줄을 전부 리스트에 넣었습니다.
날짜는 있지만 다른 값이 없는 부분은 날짜 리스트의 길이에 맞추기 위해 None으로 채웠습니다.
리스트에 None이 있는 경우에 max()함수를 쓰는 방법을 모르는 관계로 고전적으로 진행했습니다.
"""
import weather
import hw_submission

def find_tmax_idx(list):
    idx = 0
    for i in range(len(list)):
        if list[i] == None:
            pass
        elif list[idx] == None:
            idx += 1
        elif list[i] > list[idx]:
            idx = i
    return idx

def find_gapmax_idx(max, min):
    idx = 0
    for i in range(len(max)):
        if max[i] == None or min[i] == None:
            pass
        elif max[idx] == None or min[idx] == None:
            idx += 1
        elif max[i]-min[i] > max[idx]-min[idx]:
            idx = i
    return idx

def main():
    url = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filestaion = "hw/hw14/wlist.csv"
    weather.callfile(filestaion,url)
    tmax = weather.weather_float(filestaion, 4, 16, 2)
    tmin = weather.weather_float(filestaion, 3, 16, 2)
    date = weather.weather_str(filestaion, 0, 16, 2)
    tmax_idx = find_tmax_idx(tmax)
    gapmax_idx = find_gapmax_idx(tmax, tmin)
    gapmax = tmax[gapmax_idx]-tmin[gapmax_idx]

    hw_submission.submit("김성은", tmax[tmax_idx], date[tmax_idx], gapmax, date[gapmax_idx])

if __name__ == "__main__":
    main()