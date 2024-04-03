#과제
def text2list(a):
    tokens = a.split()
    result = []
    for token in tokens:
        result.append(int(token))
    return result

def average(a):
    result = sum(a)/len(a)
    return result

def median(a):
    length = len(a)//2
    result = a[length]
    return result

def main():
    input_text = "5 10 3 4 7"
    nums = text2list(input_text)
    sornums = sorted(nums)
    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(sornums)))
    print("중앙값은 {}".format(median(sornums)))
    #단 갯수가 짝수일 때는 중앙에 위치한 두 값 중 큰 값을 채택
    print(f"최솟값은 {sornums[0]}")
    print(f"최댓값은 {sornums[-1]}")

if __name__ == "__main__":
    main()
