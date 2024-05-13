#아스키코드를 이용하여 대문자는 소문자로, 소문자는 대문자로 바꾸기
#ord() = 문자를 10진수 아스키코드로 
#chr() = 10진수 아스키코드를 문자로

def toggle_text(text:str) -> str:
    aaa = list(text)
    for i in range(len(aaa)):
        aci = ord(aaa[i])
        if aci >= 97 and aci <= 122:
            aws = chr(aci - 32)
        elif aci >= 65 and aci <= 90:
            aws = chr(aci + 32)
        else:
            continue
        aaa[i] = aws
        
    res = "".join(s for s in aaa)
    return res

def main():
    txt = input("문자열입력")
    res = toggle_text(txt)
    print(res)
if __name__ == "__main__":
    main()