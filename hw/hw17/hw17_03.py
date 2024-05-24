#숨겨진 단어를 맞추는 게임(행맨)

import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text:str) -> str:
    return simpledialog.askstring(title="hangman", prompt=text)


def main():
    life = 7
    hidden_answer = "gundam"
    answer_txt = list(hidden_answer)
    shown_answer = []
    for i in range(len(answer_txt)):
        shown_answer.append("_")


    while life > 0:
        res = "".join(a+" " for a in shown_answer)

        answer = gui_input(f"남은 목숨 {life}개\n{res}")

        if answer in answer_txt:
            for i in range(len(answer_txt)):
                if answer == answer_txt[i]:
                    shown_answer[i] = answer_txt[i]
        else:
            life -= 1
        
        if not "_" in shown_answer:
            res = "".join(a for a in shown_answer)
            gui_input(f"남은 목숨 {life}개\n{res}\n정답")
            break

    if life < 1:
        gui_input(f"남은 목숨 {life}개\n{res}\n실패\n{hidden_answer}")


    

    
    

        

if __name__ =="__main__":
    main()