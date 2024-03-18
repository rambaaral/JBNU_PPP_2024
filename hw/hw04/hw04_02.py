#x, y 입력 받아서 어느 사분면인지 출력
x1=int(input("점의 x좌표를 입력해주세요."))
y1=int(input("점의 y좌표를 입력해주세요."))

if x1 == 0 or y1 == 0:
    print("점이 어느 사분면에도 속하지 않습니다.")
elif x1 > 0 and y1 > 0:
    print("점이 1사분면 위에 있습니다.")
elif x1 < 0 and y1 > 0:
    print("점이 2사분면 위에 있습니다.")
elif x1 < 0 and y1 < 0:
    print("점이 3사분면 위에 있습니다.")
elif x1 > 0 and y1 <0:
    print("점이 4사분면 위에 있습니다.")
else:
    print("올바르지 않은 접근입니다.")