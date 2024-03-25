#숫자 n이 주어졌을 때 1부터 n까지의 합을 구하는 함수 sum_n(n)만들기

def sum_n(n):
    if n > 0:
        res = (n*(n+1))/2
        print(f"1부터 {n}까지의 합은 {res:.0f}입니다.")
    else:
        print(f"{n}은(는) 유효하지 않은 숫자입니다.")

def main():
    num = int(input("1부터의 합을 알고싶은 숫자를 입력해주세요"))

    sum_n(num)

if __name__ == "__main__":
    main()