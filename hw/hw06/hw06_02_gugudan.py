#숫자를 입력받아, 구구단을 출력하는 gugugan(dan)함수 만들기

def gugudan(dan):
    if dan > 0:
        print(f"{dan}단 입니다.")
        for i in range(9):
            print(f"{dan} x {i+1} = {dan*(i+1)}")
    else:
        print(f"{dan}은(는) 유효하지 않은 숫자입니다.")

def main():
    num = int(input("보고싶은 구구단의 단을 입력해주세요"))

    gugudan(num)

if __name__ == "__main__":
    main()