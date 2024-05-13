#아스키 코드를 이용하여 카이사르 암호를 구현
#알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 대치
def caesar_encode(text:str, shift: int = 3) -> str:
    aaa = list(text)
    for i in range(len(aaa)):
        aci = ord(aaa[i])
        if aci >= 97 and aci <= 122:
            if aci+shift <=122:
                aws = chr(aci+shift)
            else:
                aws = chr(aci+shift-26)
        elif aci >= 65 and aci <= 90:
            if aci+shift <=90:
                aws = chr(aci+shift)
            else:
                aws = chr(aci+shift-26)
        else:
            continue
        aaa[i] = aws

    res = "".join(s for s in aaa)
    return res

def caesar_decode(text:str, shift: int = 3) -> str:
    aaa = list(text)
    for i in range(len(aaa)):
        aci = ord(aaa[i])
        if aci >= 97 and aci <= 122:
            if aci-shift >= 97:
                aws = chr(aci-shift)
            else:
                aws = chr(aci-shift+26)
        elif aci >= 65 and aci <= 90:
            if aci-shift >= 65:
                aws = chr(aci-shift)
            else:
                aws = chr(aci-shift+26)
        else:
            continue
        aaa[i] = aws

    res = "".join(s for s in aaa)
    return res

def main():
    fst = input("인코딩: 1\n디코딩: 2\n")
    if int(fst) == 1:
        snd = int(input("이동할 칸 수 입력"))
        trd = input("변환 할 문자 입력")
        print(f"변환전: {trd}\n변환후: {caesar_encode(trd, snd)}")
    elif int(fst) == 2:
        snd = int(input("이동할 칸 수 입력"))
        trd = input("변환 할 문자 입력")
        print(f"변환전: {trd}\n변환후: {caesar_decode(trd, snd)}")
if __name__ == "__main__":
    main()