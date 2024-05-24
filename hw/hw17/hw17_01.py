#주어진 시간을 카운트다운 하는 프로그램
#초는 반복문으로 세고 중간 중간 프로그램을 멈춰서 시간을 표현
import time

import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text:str) -> str:
    return simpledialog.askstring(title="카운트다운", prompt=text)


def main():

    try:
        tim = int(gui_input("카운트다운 시간 입력"))
        if tim > 0:
            while tim > 0:
                print(f"{tim}초\r\n")
                time.sleep(1)
                tim -= 1
            print("Boom!")
        else:
            print("유효하지 않음")
    except ValueError:
        print("유효하지 않음")

if __name__ =="__main__":
    main()