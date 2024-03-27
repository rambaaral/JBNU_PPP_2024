#연도를 주면 윤년인지 아닌지을 알려주는 함수 만들기 is_leap_year(y)
#4로 나누어 떨어지면 윤년 100으로 나누어 떨어지면 윤년 아님
def is_leap_year(y):
    if y%4 == 0 and y%100 != 0:
        return True
    else:
        return False
        
def main():
    n = int(input("년도를 입력해주세요."))
    res = is_leap_year(n)

    if n < 1:
        print("유효하지 않은 숫자입니다.")
    elif res == True:
        print(f"{n}년은 윤년입니다.")
    elif res == False:
        print(f"{n}년은 윤년이 아닙니다.")

if __name__ == "__main__":
    main()