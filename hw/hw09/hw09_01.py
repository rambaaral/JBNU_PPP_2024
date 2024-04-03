#파일 읽기
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

def readfile():
    with open("hw/hw09/hw09_01_nums.txt") as f:
        data = []
        for line in f:
            text = line.strip()
            data.extend(text2list(text))
        return data

def main():
    readfile()
    nums = readfile()
    sornums = sorted(nums)
    print(f"주어진 리스트는 {nums}")
    print(f"총 숫자의 개수는 {len(nums)}")
    print(f"평균값은 {average(sornums):.1f}")
    print(f"최솟값은 {sornums[0]}")
    print(f"최댓값은 {sornums[-1]}")
    print(f"중앙값은 {median(sornums)}")   #단 갯수가 짝수일 때는 중앙에 위치한 두 값 중 큰 값을 채택

if __name__ == "__main__":
    main()