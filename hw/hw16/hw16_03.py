#초성게임 완성하기

#ord() = 문자를 10진수 아스키코드로 
#chr() = 10진수 아스키코드를 문자로

import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text:str) -> str:
    return simpledialog.askstring(title="초성게임", prompt=text)


cs_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

joongs_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

jongs_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def get_cs(aws):
    dataset = []
    aaa = list(aws)
    for tokens in aaa:
        token = (ord(tokens)-ord("가"))//588
        dataset.append(cs_list[token])
    res = "".join(s for s in dataset)
    return res

def main():
    hidden = "핵산말단분해효소"
    problem = get_cs(hidden)

    answer = gui_input(f"문제의 초성은 '{problem}'입니다.\n답은?\n")
    if answer == hidden:
         print("정답")
    else:
        print("오답")
        
if __name__ == "__main__":
    main()