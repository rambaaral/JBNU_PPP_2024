#숫자 입력 받아서 그 리스트 출력
#숫자는 정수만 입력, 자연수가 아니면 무시
#-1입력시 결과 출력
def make_int_list():
    dataset = []
    while not -1 in dataset:
        aaa = input("X=?")
        try:
            if int(aaa) > 0 or int(aaa) == -1:
                dataset.append(int(aaa))
        except ValueError:
            continue

    dataset.pop()
    return dataset

def main():
    list = make_int_list()

    print(f'입력된 값은 {list}입니다. 총 {len(list)}개의 자연수가 입력되었고, 평균은 {sum(list)/len(list)}입니다.')

if __name__ == "__main__":
    main()