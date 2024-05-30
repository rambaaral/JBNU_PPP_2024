#카이사르 암호 gui
import tkinter as tk

def caesar_encode():
    aaa = list(str(inoutput1.get(1.0, tk.END)))
    bbb = int(input1.get()) % 26
    for i in range(len(aaa)):
        aci = ord(aaa[i])
        if aci >= 97 and aci <= 122:
            if aci+bbb <=122:
                aws = chr(aci+bbb)
            else:
                aws = chr(aci+bbb-26)
        elif aci >= 65 and aci <= 90:
            if aci+bbb <=90:
                aws = chr(aci+bbb)
            else:
                aws = chr(aci+bbb-26)
        else:
            continue
        aaa[i] = aws

    res = "".join(s for s in aaa)
    inoutput2.delete(1.0, tk.END)
    inoutput2.insert(tk.END, res)

def caesar_decode():
    aaa = list(str(inoutput2.get(1.0, tk.END)))
    bbb = int(input1.get()) % 26
    for i in range(len(aaa)):
        aci = ord(aaa[i])
        if aci >= 97 and aci <= 122:
            if aci-bbb >= 97:
                aws = chr(aci-bbb)
            else:
                aws = chr(aci-bbb+26)
        elif aci >= 65 and aci <= 90:
            if aci-bbb >= 65:
                aws = chr(aci-bbb)
            else:
                aws = chr(aci-bbb+26)
        else:
            continue
        aaa[i] = aws

    res = "".join(s for s in aaa)
    inoutput1.delete(1.0, tk.END)
    inoutput1.insert(tk.END, res)

def main():
    global inoutput1, input1,inoutput2

    window = tk.Tk()
    window.title("카이사르 암호")
    window.geometry("640x400+100+100")

    frame = tk.Frame(window)
    frame.pack(fill=tk.BOTH, expand=True)



    label1 = tk.Label(frame, text="평문")
    
    inoutput1 = tk.Text(frame, width=20, height=5)
    
    button1 = tk.Button(frame, text="암호화", command=caesar_encode)
    
    label_input1 = tk.Label(frame, text="시프트 수")

    input1 = tk.Entry(frame, width=5)
    
    button2 = tk.Button(frame, text="복호화", command=caesar_decode)

    label2 = tk.Label(frame, text="암호문")
    
    inoutput2 = tk.Text(frame, width=20, height=5)
    


    label1.grid(row=0, column=0, padx=5, pady=5, sticky="n")
    inoutput1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    button1.grid(row=1, column=1, padx=5, pady=5)
    label_input1.grid(row=0, column=2, padx=5, pady=5, sticky="n")
    input1.grid(row=1, column=2, padx=5, pady=5)
    button2.grid(row=1, column=3, padx=5, pady=5)
    label2.grid(row=0, column=4, padx=5, pady=5, sticky="n")
    inoutput2.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")


    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(4, weight=1)


    window.mainloop()


if __name__ == "__main__":
    main()