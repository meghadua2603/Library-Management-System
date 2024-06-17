import mysql.connector as a
con=a.connect(host="localhost", user="root",passwd="meghadua",database="lib2")

def books():
          bname=input("enter book name:")
          bco=input("enter book code:")
          total=input("total books:")
          subject=input("enter subject:")
          data=(bname,bco,total,subject)
          sql='insert into books values(%s,%s,%s,%s)'
          c=con.cursor()
          c.execute(sql,data)
          con.commit()
          print(">__________________________________________________<")
          print("data entered successfully")
          main()

def issue():
          name=input("enter name:")
          regno=input("enter reg no:")
          bcode=input("enter book code:")
          issuedate=input("enter date(eg:22/02/22):")
          abc='insert into issue values(%s,%s,%s,%s)'
          data=(name,regno,bcode,issuedate)
          c=con.cursor()
          c.execute(abc,data)
          con.commit()
          print("book issued to:",name)
          main()

          
def submit():
          name=input("enter name:")
          regno=input("enter reg no:")
          bcode=input("enter book code:")
          submitd=input("enter date(eg:22/02/22):")
          abc='insert into submit values(%s,%s,%s,%s)'
          data=(name,regno,bcode,submitd)
          c=con.cursor()
          c.execute(abc,data)
          con.commit()
          print("book submitted by:",name)
          main()
         

def delbook():
          bco=input("enter book code:")
          a="delete from books where bcode=%s"
          data=(bco,)
          c=con.cursor()
          c.execute(a,data)
          con.commit()
          main()

def displayb():
          a="select* from books"
          c=con.cursor()
          c.execute(a)
          myresult=c.fetchall()
          for i in myresult:
                    print("book name:",i[0])
                    print("book code:",i[1])
                    print("total:",i[2])
                    print("subject:",i[3])
                    main()
          

def main():
          print("""
  
                               LIBRARY MANAGER
1.ADD BOOK
2.ISSUE BOOK
3.SUBMIT BOOK
4.DELETE BOOK
5.DISPLAY BOOKS
""")
          choice = input ("Enter Task No :")
          if (choice =='1'):
                    books()
          elif (choice=='2'):
                    issue()
          elif (choice=='3'):
                    submit()
          elif (choice=='4'):
                    delbook()
          elif (choice=='5'):
                    displayb()
          else :
                    print("Wrong choice")
                    main ()
def pswd():
          passs = input ("Enter Password:")
          if passs =="123":
                    main ()
          else :
                    print("Wrong Password")
                    pswd ()
pswd()
