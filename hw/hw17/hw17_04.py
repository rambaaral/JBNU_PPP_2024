#로또번호 추출기
import random
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text:str) -> str:
    return simpledialog.askstring(title="test", prompt=text)


def main():
    try:
        cnt = int(gui_input("로또 추천 횟수 입력"))
        while cnt > 0:
            dataset = []
            while len(dataset) < 6:
                aaa = random.randint(1,45)
                if not aaa in dataset:
                    dataset.append(aaa)
            print(sorted(dataset))
            cnt -= 1
    except ValueError:
        print("유효하지 않은 값")

if __name__ =="__main__":
    main()