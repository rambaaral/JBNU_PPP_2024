#삼각함수 표 만들기
import math
print("각        라디안       sin         cos         tan")
for i in range(11):
    n = math.radians(i)
    print(f"{i}         {n:.4f}      {(math.sin(n)):.4f}      {(math.cos(n)):.4f}      {(math.tan(n)):.4f}")