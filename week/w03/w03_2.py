#포맷팅
aaaaa = 3.14159362
print('asdf{:.3f}'.format(aaaaa))
print(f'asdf{aaaaa:.3f}')

#반복문 for, while
#for는 주어진 리스트를 모두 소진할 동안 반복
#while은 주어진 조건이 참일 때 게속 실행
#반복문을 특정 조건에 멈출 경우 break나 continue를 사용한다.
#break는 반복문을 완전히 멈춰버리고 continue는 중간에 반복문을 다시 시작한다.

#1부터 10까지 합
resu = 0 # 결과 함수를 반복문 밖에 둬야 리셋되지 않는다.
for i in range(10):
    #aaaa = 0
    #resu = 0
    resu = resu + (i+1)
    #for j in range(i+1):
        #aaaa = aaaa + (j+1)
    #resu = resu + aaaa
print(resu)

#구구단
for i in range(10):
    print(f'2*{i}={i*2}')

#범위 안 짝수의 합
aaa = 0
for i in range(250):
    if (i+1)%2==0:
        aaa = aaa + (i+1)
    else:
        continue
print(aaa)

#반복문에 사전형 섞기

mart = {"우유":2800, "계란":300, "빵":1200, "물": 1700}
cart = ["물", "물", "계란", "빵", "빵", "빵"]
cost = 0
for item in cart:
    cost += mart[item]
print(f'{cost:,}원')
