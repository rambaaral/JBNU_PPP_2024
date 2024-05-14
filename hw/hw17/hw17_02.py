#구구단 문제를 제출하고 정답 개수를 체크해서 점수 출력
import random

def make_exam(num):
    exam = []
    answ = []
    i = 0
    while i < num:
        aaa = random.randint(1, 9)
        bbb = random.randint(1, 9)

        exam.append(f"{aaa}X{bbb}=?\n")
        answ.append(aaa*bbb)

        i += 1
    
    return exam, answ

def do_exam(exam, answer):
    dataset = []

    for i in range(len(exam)):
        aaa = int(input(exam[i]))
        if aaa == answer[i]:
            dataset.append(1)
        else:
            dataset.append(0)
    
    return dataset

def main():
     exams = int(input("문제 갯수 입력"))
     exam, answer = make_exam(exams)

     result = do_exam(exam, answer)

     print(f"시험 결과는 {100*sum(result)/len(result):.1f}점")


if __name__ =="__main__":
    main()