#참 거짓
#if 조건문, and 혹은 or 써서 복합 조건 가능
import math
x1=0
y1=0
x2=3
y2=4

dist = math.sqrt((x2-x1)**2+(y2-y1)**2)

if (dist <= 1):
    print("거리는 {}입니다. 두 점이 너무 가깝습니다.".format(dist))
else:
    print("거리는 {}입니다.".format(dist))

#정수, 실수
fl=4

if fl % 2 == 1:
    print("홀수입니다.")
else:
    print("짝수입니다.")
 
#문자열 함수 따로 찾아보기 아마도 교재에 있을듯
#\\백슬레시, \'작은따옴표, \"큰따옴표, \n 개행문자, \r 개행문자, \t탭문자
text = "abcdefghijklnmopqrstuvwxyz"
print('입력한 문자는 "{}"입니다.'.format(text))
print(len(text))
print(text.upper())#upper 괄호 안에는 아무것도 못 씀
#문자열에 숫자를 곱하면 문자열을 숫자만큼 반복함
print("r"*5)
print(text[:3])
print(text[-2:])

#리스트, 튜플, 레인지 튜플은 대괄호 대신에 괄호 사용
print(text[4])#인덱스는 0부터 시작함
#콜론은 범위를 뜻함 :n=왼쪽부터 몇번쨰까지, n:몇번째부터 끝까지(n+1부터 시작함), ::n=몇번째만 출력
print(text[2:6])
print(text[::4])
#문자열 뒤집기
print(text[::-1])
#실습 리스트 파악해두기

#사전형 딕셔너리
eo=1
es=2
eb=3
cal = {"한라봉": 50, "딸기": 34, "바나나": 77}
total_cal = cal["한라봉"]*eo+cal["딸기"]*es+cal["바나나"]*eb
print(total_cal)

#셋(집합)
#중복 데이터가 안들어가지만 순서가 보장되지 않음
#print format
#round는 반올림하면서 숫자를 버리지만 print format은 버리지 않고 잘라서 출력한다.
sss=math.pi
print("asdfsd{:7.10f}".format(sss))
print(f'{sss:.3f}')



