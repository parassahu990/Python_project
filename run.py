import mysql.connector as my
import admin, user
con = my.connect(host="localhost",user="root",passwd="",database="ticket")

def panel():
    while True:
        print("-"*10,"BUS TICKET BOOKING SYSTEM","-"*10)
        print("enter 1 for admin pannel")
        print("enter 2 for user pannel")
        print("enter 3 to exit")
        ch=int(input("enter your choice "))
        try:
            if ch==1:
                admin.menu()
            elif ch==2:
                user.menu()
            elif ch == 3:
                panel()
            else:
                print("invalid choice")
        except:
            print("please enter right value")
panel()

