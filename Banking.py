import mysql.connector
from datetime import date 

def clear(): 
    for _ in range(65): 
        print()

def account_status(acno): 
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'bank_project',
        user = 'root',
        password = '206244'
    ) 
    cursor = conn.cursor() 
    sql = "select status, balance from customer where acno ='" + acno + "'" 
    result = cursor.execute(sql) 
    result = cursor.fetchone() 
    conn.close() 
    return result 

def deposit_amount(): 
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'bank_project',
        user = 'root',
        password = '206244'
    ) 
    cursor = conn.cursor() 
    clear() 
    acno = input('Enter account No :') 
    amount = input('Enter amount :') 
    today = date.today() 
    result = account_status(acno)
    if result [0] == 'active': 
        sql1 = "update customer set balance = balance+"+amount+ ' where acno = '+acno+' and status="active";'
        sql2 = 'insert into transaction(amount, type, acno, dot) values(' + amount +',"deposit",'+acno+',"'+str(today)+'");'
        cursor.execute(sql2)
        cursor.execute(sql1) 
        print('\n\namount deposited')
    else:
        print('\n\nClosed or Suspended Account....') 
    wait = input('\n\n\n Press any key to continue....') 
    conn.close() 

def withdraw_amount(): 
    conn = mysql.connector.connect(
         host = 'localhost',database = 'bank_project',user = 'root',password = '206244') 
    cursor = conn.cursor() 
    clear() 
    acno = input('Enter account No :') 
    amount = input('Enter amount :') 
    today = date.today() 
    result = account_status(acno) 
    if result [0] == 'active'and int(result [1]) >= int(amount):
        sql1 = "update customer set balance = balance-" +amount+ ' where acno = '+acno+' and status="active";'
        sql2 = 'insert into transaction(amount, type, acno, dot) values('+amount+', "withdraw",'+acno+',"'+str(today)+'");'
        cursor.execute(sql2)
        cursor.execute(sql1)
        print('\n\namount withdrawn')
    else: print('\n\nClosed or Suspended Account.Or Insufficient amount')
    wait = input('\n\n\n Press any key to continue....')
    conn.close()

def transaction_menu():
    while True:
        clear()
        print(' Trasaction Menu')
        print("\n1. Deposit Amount")
        print('\n2. WithDraw Amount')
        print('\n3. Back to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice...: '))
        if choice == 1:
            deposit_amount()
        if choice== 2:
            withdraw_amount()
        if choice ==3:
            break

def search_menu():
    conn = mysql.connector.connect(
        host='localhost', database='bank_project', user='root', password='206244')
    cursor = conn.cursor()
    while True:
        clear()
        print(' Search Menu')
        print("\n1. Account No")
        print('\n2. Aadhar card')
        print('\n3. Phone No')
        print('\n4. Email')
        print('\n5. Names')
        print('\n6. Back to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice...: '))
        field_name=' '
        if choice == 1:
            field_name = 'acno'
        if choice == 2:
            field_name = 'aadhar_no'
        if choice == 3:
            field_name = 'phone'
        if choice == 4:
            field_name = 'email'
        if choice == 5:
            field_name = 'name'
        if choice ==6:
            break
        msg ='Enter '+field_name+': '
        value = input(msg)
        if field_name=='acno':
            sql = 'select * from customer where '+field_name +  '= '+value+';'
        else:
            sql = 'select * from customer where '+field_name +' like "%'+value+'%";'
        #print(sql)
        cursor.execute(sql)
        records = cursor.fetchall()
        n = len(records)
        clear()
        print('Search Result for ', field_name, ' ',value)
        print('-'*80)
        for record in records:
            print(record[0], record [1], record [2], record [3],
                  record[4], record [5], record [6], record [7], record[8])
        if(n <= 0):
            print(field_name, ' ', value, 'does not exist')
        wait= input('\n\n\n Press any key to continue....')
    conn.close()
    wait=input('\n\n\n Press any key to continue....')

def account_details():
    clear()
    acno = input('Enter account no :')
    conn = mysql.connector.connect(
        host='localhost', database ='bank_project', user ='root', password='206244')
    cursor = conn.cursor()
    sql='select * from customer where acno = '+acno+';'
    sql1='select tid, dot, amount, type from transaction t where t.acno='+acno+';'
    cursor.execute(sql)
    result = cursor.fetchone()
    clear()
    print('Account Details')
    print('-' * 120) 
    print('Account No :', result [0]) 
    print('Customer Name:', result [1])
    print('Address :', result [2]) 
    print('Phone NO :', result [3]) 
    print('Email ID :', result [4]) 
    print('Aadhar No :', result [5]) 
    print('Account Type:', result [6]) 
    print('Account Status :', result [7])
    print('Current Balance :', result [8]) 
    print('-' * 120) 
    cursor.execute(sql1) 
    results = cursor.fetchall() 
    for result in results: 
        print(result [0], result [1], result [2], result [3]) 
    conn.close() 
    wait = input('\n\n\nPress any key to continue.....') 

def add_account(): 
    conn = mysql.connector.connect(
        host = 'localhost',database ='bank_project', user=' root ', password='206244')
    cursor = conn.cursor()

    name = input('Enter Name :')
    addr= input('Enter address :')
    phone = input('Enter Phone no :')
    email = input('Enter Email :')
    aadhar = input('Enter Aadhar no :')
    actype = input('Account Type (saving/current) :')
    balance = input('Enter opening balance :')
    sql = 'insert into customer(name,address,phone,email,aadhar_no,acc_type,balance,status) values("'+ name +'", "'+ addr+'", "'+phone+'","'+email+'","'+aadhar+'","'+actype+'","'+balance+'", "active");'
    #print(sql)
    cursor.execute(sql)
    conn.close()
    print('\n\nNew customer added successfully')
    wait=input('\n\n\nPress any key to continue.....')

def modify_account(): 
    conn = mysql.connector.connect(
        host = 'localhost',database = 'bank_project', user=' root ', password='206244')
    cursor = conn.cursor()
    clear()
    acno = input(' Enter customer Account No :')
    print('Modify screen ') 
    print('\n1.Customer Name ')
    print('\n2.Customer Address ') 
    print('\n3.Customer Phone No ') 
    print('\n4.Customer Email ID ') 
    print('\n\n')
    choice= int(input('What do you want to change?'))
    new_data = input('Enter New value :') 
    field_name =''
    if choice== 1:
        field_name =' name '
    if choice ==2:
        field_name = ' address '
    if choice == 3:
        field_name = ' phone '
    if choice == 4:
        field_name = ' email '
    sql ='update customer set' + field_name + '="' + new_data + '" where acno=' + acno + ';'
    #print(sql)
    cursor.execute(sql)
    print('\n\nCustomer Information modified..')
    wait= input('\n\n\n Press any key to continue....')

def close_account():
    conn = mysql.connector.connect(
        host=' localhost ', database=' bank_project ', user=' root ', password='206244')
    cursor = conn.cursor()
    clear()
    acno = input('Enter customer Account No :')
    sql ='update customer set status="close" where acno = ' + acno + ';' 
    cursor.execute(sql) 
    print('\n\nAccount closed') 
    wait = input('\n\n\n Press any key to continue....') 
    
def activate_account():
    conn = mysql.connector.connect(
        host = 'localhost',database = 'bank_project',user = 'root',password = '206244') 
    cursor = conn.cursor() 
    clear() 
    acno=input('Enter customer Account No :') 
    sql = 'update customer set status="active" where acno ='+acno+';' 
    cursor.execute(sql) 
    print('\n\nAccount Activated') 
    wait = input('\n\n\nPress any key to continue....') 

def main_menu(): 
    while True: 
        clear() 
        print(' Main Menu')
        print("\n1. Add Account")
        print('\n2. Modify Account')
        print('\n3. Close Account')
        print('\n4. Activate Account')
        print('\n5. Transaction Menu')
        print('\n6. Search Menu')
        print('\n7. Close application')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        if choice == 1:
            add_account()
        if choice== 2:
            modify_account()
        if choice ==3:
            close_account()
        if choice == 4:
            activate_account()
        if choice ==5 :
            transaction_menu()
        if choice ==6 :
            search_menu()
        if choice == 7:
            break

if __name__== "__main__":
    main_menu()