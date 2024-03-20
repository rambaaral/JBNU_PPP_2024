#삼각형 별 그리기
n = int(input("별의 개수를 입력해주세요"))

if n > 0:
    for i in range(n):
        print('*'*(i+1))
elif n < 0:
    n = abs(n)
    for i in range(n):
        print('*'*(n-i))
else:
    print("유효하지 않은 숫자입니다.")