import time
import datetime
user='benish'
pass1='123456'
def login():
    attempt=1
    for j in range(5):
        for i in range(1,4):
            login = input("Enter the user name: ")
            password = input("Enter the password: ")
            if login==user and password==pass1 and len(user)==6 and len(pass1)==6:
                print("Valid Data You the access the page")
                break
            else:
                f=open('store.txt', 'a')
                f.write(f'Incorrect username: {login}\n Incorrect password: {password}\n')
                current_time = datetime.datetime.now()
                f.write(f'current date and time is {current_time}\n')
                f.close()
                print('Wrong password or username')
                print("No of wrong attempts you made is ",attempt)
                attempt+=1
        if login==user and password==pass1:
            break
        elif i==3:
            print('wait for 3 sec')
            time.sleep(3)

