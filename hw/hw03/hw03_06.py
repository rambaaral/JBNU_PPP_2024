#두 지점 사이 거리 구하기
x1=int(input("첫 번째 점의 x좌표를 입력해주세요."))
y1=int(input("첫 번째 점의 y좌표를 입력해주세요."))
x2=int(input("두 번째 점의 x좌표를 입력해주세요."))
y2=int(input("두 번째 점의 y좌표를 입력해주세요."))
import math
le=round(math.sqrt(((x1-x2)**2)+((y1-y2)**2)), 2)

print("두 점 사이의 거리는 {}입니다.".format(le))