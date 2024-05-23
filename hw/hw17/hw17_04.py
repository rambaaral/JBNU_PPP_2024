#로또번호 추출기


import random

def main():
    cnt = int(input("로또 추천 횟수 입력"))
    while cnt > 0:
        dataset = []
        while len(dataset) < 6:
            aaa = random.randint(1,45)
            if not aaa in dataset:
                dataset.append(aaa)
        print(sorted(dataset))
        cnt -= 1

if __name__ =="__main__":
    main()