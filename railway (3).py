import mysql.connector as m

pnr = 999
mydb = m.connect(host="localhost", user="root", passwd="tiger", database="train")
mycursor=mydb.cursor()

def railresmenu():
                print("***********************")
                print("******MAIN MENU********")
                print("***********************")
                print("Train Reservation System ")
                print("1.Add Train Detail")
                print("2.Reservation of Ticket")
                print("3.Cancellation of Ticket")
                print("4.Display PNR status")
                print("5.Exit")
                print("***********************")
                n=int(input("Enter your choice"))
                if(n==1):
                                traindetail()
                elif(n==2):
                                reservation()
                elif(n==3):
                                cancel()
                elif(n==4):
                                displayPNR()
                elif(n==5):
                                exit(0)
                else:
                                print("Invalid Choice")
                 
                
def traindetail():
                print("******Train Details*******")
                ch='y'
                while (ch=='y'):
                                l=[]
                                tnum=int(input("Enter train number :"))
                                l.append(tnum)
                                tname=input("Enter train name :")
                                l.append(tname)
                                ac1=int(input("Enter number of seats in first AC :"))
                                l.append(ac1)
                                ac2=int(input("Enter number of seats in second AC : "))
                                l.append(ac2)
                                ac3=int(input("Enter number of of seats in third AC :"))
                                l.append(ac3)
                                slp=int(input("Enter number of of seats in sleeper :"))
                                l.append(slp)
                                train=(l)
                                sql="insert into traindetail(tnum,tname,ac1,ac2,ac3,slp)values(%s,%s,%s,%s,%s,%s)"
                                mycursor.execute(sql,train)
                                mydb.commit()
                                print("Record Added Successfully")
                                print("Do you want to add more train records")
                                ch=input("YES-y/NO")
                print('\n' *10)
                print("*******************************************************************")
                print("*******************************************************************")
                railresmenu()

def reservation():
                global pnr
                l1 = []
                print("*******************************************************************")
                print("*********************PASSENGER DETAIL ENTRY ***********************")
                print("*******************************************************************")
                pname=input("\t\t\tEnter passenger name :->")
                l1.append(pname)
                age=input("\t\t\tEnter age of passenger : ->")
                l1.append(age)
                trainno=input("\t\t\tEnter the train number  :->")
                l1.append(trainno)
                np=int(input("\t\t\tEnter number of passangers :->"))
                l1.append(np)
                print("\n\t\t\t\Select the class of travel  --> ")
                print("1.AC FIRST CLASS")
                print("2.AC SECOND CLASS")
                print("3.AC THIRD CLASS")
                print("4.SLEEPER CLASS")
                cp=int(input("Enter your choice:"))
                if(cp==1):
                                amount=np*1000
                                cls='ac1'
                elif(cp==2):
                                amount=np*800
                                cls='ac2'
                elif(cp==3):
                                amount=np*500
                                cls='ac3'
                else:
                                amount=np*350
                                cls='slp'
                l1.append(cls)           
                print("*********************************")
                print("Total amount to be paid:", amount)
                print("*********************************")
                l1.append(amount)
                pnr=pnr+1
                print("PNR Number:",pnr)
                print("Status: Confirmed")
                sts='conf'
                l1.append(sts)
                l1.append(pnr)
                train1=(l1)
                sql="insert into passengers(pname,age,trainno,noofpas,cls,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(sql,train1)
                mydb.commit()
                print("insertion completed")
                print("Go back to menu")
                print('\n' *10)

                print("===================================================================")
                railresmenu()
                railresmenu()

def cancel():
                print("Ticket cancel window")
                pnr=input("enter PNR for cancellation of Ticket")
                pn=(pnr,) 
                sql="update passengers set status='deleted' where pnrno=%s"
                mycursor.execute(sql,pn)
                mydb.commit()
                print("Deletion completed")
                print("Go back to menu")
                print('\n' *10)

                print("===================================================================")
                railresmenu()
                railresmenu()

def displayPNR():
                print("PNR STATUS window")
                pnr=input("enter PNR NUMBER")
                pn=(pnr,) 
                sql="select * from passengers where pnrno=%s"
                mycursor.execute(sql,pn)
                res=mycursor.fetchall() 
                print("PNR STATUS are as follows : ")
                print("(pname,age,trainno, noofpas,cls,amt,status, pnrno)")
                for x in res:
                                print(x)   
                print("Go back to menu")
                print('\n' *10)

                print("===================================================================")
                railresmenu()

railresmenu()
