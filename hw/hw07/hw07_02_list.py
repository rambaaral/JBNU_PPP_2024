#1-n까지 리스트를 돌려주는 함수 만들기get_range_list(n)
def get_range_list(n):
    lis = []
    for i in range(n):
        lis.append(i+1)
    return lis

def main():
    x = int(input("숫자를 입력해주세요"))
    res = get_range_list(x)
    
    if x < 1:
        print("유효하지 않은 숫자입니다.")
    else:
        print(f"1부터 {x}까지의 리스트 입니다.")
        print(res)


if __name__ == "__main__":
    main()