#예외처리
#try함수? 첨보네
def str2float(text:str, default_value:float = -999) -> float:
    try:
        return float(text)
    except ValueError:
        return default_value
    
def main():
    print(str2float(input("입력")))
if __name__ == "__main__":
    main()