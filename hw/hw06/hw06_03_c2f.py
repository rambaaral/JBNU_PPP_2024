#섭씨를 화씨로 바꾸는 함수 c2f(t_c)함수 만들기

def c2f(t_c):
    n = t_c*9/5 + 32
    print(f"{t_c:.1f}℃ 는 {n:.1f}℉ 입니다.")

def main():
    deg = float(input("화씨(℉ )로 바꾸고싶은 온도를 섭씨(℃ )로 입력해주세요"))

    c2f(deg)

if __name__ == "__main__":
    main()