#파일을 무조건 다운받으면 훨씬 느려질 수 있다.

#"코드스페이스"에서 내 코드가 import되지 않을 때 맨 윗줄에 추가
# import sys
# if "./" not in sys.path:
#     sys.path.append("./")
#그럼 난 쓸 필요 없는거 아닌가

#따옴표 3개씩 쓰면 그 안에 있는 문자열은 다 주석같은 느낌
#파일 초반에 함수에 대한 설명을 넣는 용도로 자주 쓰임

#회사마다 파이썬을 사용할 때 작성 스타일이 다르다.
#작성 규격까지 정해져있는듯

#함수의 설계
# def download(filename):
# def download(filename, URL):
# def download(filename, year):
# def download(filename, station, year)
#자신이 필요한 요소를 생각하고 함수의 매개변수를 만들자
#인자는 매개변수의 인자

# def download(filename, year=[2021]):
#이런식으로 선언해두면 기본값이 된다. 함수를 사용할 때 지정하면 바뀌지만 지정하지 않아도 함수 사용 가능
# def download(filename, year=None):
#     if year is None:
#         year = [2021]
#보통은 이렇게 쓴다?

#전역변수와 지역변수
#전역변수: 함수 밖, 전역 이름공간에 정의된 변수
#지역변수: 함수 안, 지역 이름공간에 정의된 변수
#지역변수는 그 변수가 정의된 함수 안에서만 읽을 수 있다.
#전역변수는 프로그램 어디서든 읽을 수 있다. 단, 함수 안에서 전역변수에 새로운 값을 대입할 수 없다.
#이거 글로벌 지정 그거인가보네

#람다 식
# f = lambda asdf: 1234

# def f(asdf):
#     return 1234
#위에 두 가지 문법은 같은 기능을 가지고 있다.
#지능형 함수 사용하면 함수를 완전히 한 문장으로 만들 수 있을듯

#패킹과 언패킹
#문자열에서 포맷 사용할 때 한 함수 내의 리턴값에서 전부 가져올 수 있다면
#*함수()를 포맷 안에 넣으면 한번에 다수의 칸에 넣을 수 있다.

#파일 저장시 확장자
#앞으로 csv와 html확장자로 파일을 저장하게 될거임
#csv와 html은 줄바꿈 기호가 다르기 때문에 데이터 읽기의 난이도가 어려워질 것임

# 타입 힌트
# def download(filename:str, station:int, year:list)
# 이런식으로 매개변수의 타입을 정해둘 수 있음 이 상태로 기본값 지정도 가능함

#data class와 NamedTuple
#자신이 변수의 타입을 만들 수 있다.


def main():
    pass
if __name__ == "__main__":
    main()