#coding=utf8
from account import BankAccount

bank1 = BankAccount('dg','12345',500)


while True:
    count = input('请选择你的操作\n1:查询余额\n2:存钱\n3:取钱\n')
    if count.isdigit():
        count = int(count)
        if count == 1:
            print(bank1)
        elif count == 2:
            while True:
                money = input('请输入要存储的额度:')
                if money.isdigit():
                    money = int(money)
                    bank1.save(money)
                    print('存钱成功')
                    break
                else:
                    print('输入有误，请重新输入！')
                    continue
        elif count == 3:
            while True:
                money = input('请输入要取的金额:')
                if money.isdigit():
                    money = int(money)
                    if money > bank1.balance:
                        print('余额不足请重新输入！')
                    else:
                        bank1.withdraw(money)
                        print('取钱成功')
                        break
                else:
                    print('输入有误，请重新输入！')
                    continue

    elif count == 'q':
        print(bank1)
        break

    else:
        print('输入有误，请重新输入！')
