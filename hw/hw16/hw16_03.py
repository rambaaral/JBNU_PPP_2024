#초성게임 완성하기

#ord() = 문자를 10진수 아스키코드로 
#chr() = 10진수 아스키코드를 문자로

def get_cs(aws):
    return "ㅍㅇㅅ"

def main():
    ha = "프원실"
    problem = get_cs(ha)
    print(f"문제의 초성은 '{problem}'입니다.")

    answer = input("답은?")
    if answer == ha:
        print("정답")
    else:
        print("오답")



if __name__ == "__main__":
    main()