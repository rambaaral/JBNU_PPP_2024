import tkinter as tk
import csv
import random

# CSV 파일 경로
CSV_FILE = 'hw/hw22/accounts.csv'

# 계좌 정보를 저장하기 위한 클래스
class Account:
    def __init__(self, account_number, password, balance=0):
        self.account_number = account_number
        self.password = password
        self.balance = balance

# 계좌 정보를 CSV 파일에 저장하는 함수
def save_account(account):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([account.account_number, account.password, account.balance])

# CSV 파일에서 모든 계좌 정보를 불러오는 함수
def load_accounts():
    accounts = {}
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                account_number, password, balance = row
                accounts[account_number] = Account(account_number, password, int(balance))
    except FileNotFoundError:
        pass
    return accounts

# 모든 계좌 정보를 CSV 파일에 저장하는 함수
def save_all_accounts(accounts):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for account in accounts.values():
            writer.writerow([account.account_number, account.password, account.balance])

# 계좌 생성 함수
def create_account():
    account_number = ''.join(str(random.randint(0, 9)) for _ in range(12))
    password = ''.join(str(random.randint(0, 9)) for _ in range(4))
    new_account = Account(account_number, password)
    save_account(new_account)
    update_entries(account_number, password, 0)

# 공통적으로 엔트리 업데이트하는 함수
def update_entries(account_number, password, balance):
    account_number_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    balance_entry.delete(0, tk.END)
    account_number_entry.insert(0, account_number)
    password_entry.insert(0, password)
    balance_entry.insert(0, balance)

# 잔액 조회 함수
def check_balance():
    account_number = account_number_entry.get()
    password = password_entry.get()
    accounts = load_accounts()

    if account_number in accounts and accounts[account_number].password == password:
        balance = accounts[account_number].balance
        balance_entry.delete(0, tk.END)
        balance_entry.insert(0, balance)
    else:
        balance_entry.delete(0, tk.END)
        balance_entry.insert(0, "오류")

# 입금 함수
def deposit():
    account_number = account_number_entry.get()
    amount = int(balance_entry.get())
    accounts = load_accounts()

    if account_number in accounts:
        accounts[account_number].balance += amount
        save_all_accounts(accounts)
        balance_entry.delete(0, tk.END)
        balance_entry.insert(0, accounts[account_number].balance)
    else:
        balance_entry.delete(0, tk.END)
        balance_entry.insert(0, "오류")

# 출금 함수
def withdraw():
    account_number = account_number_entry.get()
    password = password_entry.get()
    amount = int(balance_entry.get())
    accounts = load_accounts()

    if account_number in accounts and accounts[account_number].password == password:
        if accounts[account_number].balance >= amount:
            accounts[account_number].balance -= amount
            save_all_accounts(accounts)
            balance_entry.delete(0, tk.END)
            balance_entry.insert(0, accounts[account_number].balance)
        else:
            balance_entry.delete(0, tk.END)
            balance_entry.insert(0, "잔액 부족")
    else:
        balance_entry.delete(0, tk.END)
        balance_entry.insert(0, "오류")

def main():
    global account_number_entry, password_entry, balance_entry
    # Tkinter GUI 설정
    root = tk.Tk()
    root.title("은행 관리 시스템")

    # 계좌 생성
    create_button = tk.Button(root, text="계좌 생성", command=create_account)
    create_button.pack()

    # 계좌번호, 비밀번호, 금액 Entry
    tk.Label(root, text="계좌번호").pack()
    account_number_entry = tk.Entry(root)
    account_number_entry.pack()

    tk.Label(root, text="비밀번호").pack()
    password_entry = tk.Entry(root)
    password_entry.pack()

    tk.Label(root, text="금액").pack()
    balance_entry = tk.Entry(root)
    balance_entry.pack()

    # 잔액 조회 버튼
    check_balance_button = tk.Button(root, text="조회", command=check_balance)
    check_balance_button.pack()

    # 입금 버튼
    deposit_button = tk.Button(root, text="입금", command=deposit)
    deposit_button.pack()

    # 출금 버튼
    withdraw_button = tk.Button(root, text="출금", command=withdraw)
    withdraw_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
