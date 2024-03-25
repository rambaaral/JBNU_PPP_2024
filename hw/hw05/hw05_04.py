#삼각함수 표 만들기
#탄젠트는 90도 넘어가면 무한이니까 조치가 필요할듯
import math
print(f'{"각":^2} {"라디안":^6} {"sin":^6} {"cos":^6} {"tan":^6}')
for i in range(11):
    n = math.radians(i)
    print(f"{i} {n:6.4f} {(math.sin(n)):6.4f} {(math.cos(n)):6.4f} {(math.tan(n)):6.4f}")