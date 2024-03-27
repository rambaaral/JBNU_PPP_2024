#숫자 리스트를 매개변수로 받아서 평균을 구하시오. 함수는 average(nums)
def average(nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return sum/len(nums)


def main():
    x = [1,2,3,4,5,6,7,8,9,10]
    res = average(x)
    print(f"평균은 {res}이다.")



if __name__ == "__main__":
    main()