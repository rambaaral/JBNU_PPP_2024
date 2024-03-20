#숫자를 입력받아, 입력받은 숫자의 구구단을 출력하시오
n = int(input("자연수를 입력해주세요"))

print(f"{n}단의 구구단입니다.")

for i in range(9):
    print(f'{n}*{(i+1)}={(i+1)*n}')
