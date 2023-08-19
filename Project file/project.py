import tkinter as tk
from tkinter import *
import mysql.connector as mc
from tkinter import ttk
import time
import datetime
import random

#-----------------------------------------------------------------------------------------------------------------
proj=tk.Tk()
proj.geometry('1200x700')
proj.title('TrainMachan.com')
proj.iconbitmap('train.ico')
frame=Frame(proj)
frame.pack(fill=BOTH)
pic=PhotoImage(file='train4.png')
label=Label(frame,image=pic)
label.pack(fill=BOTH)

#-----------------------------------------------Date & Time------------------------------------------------------------------
def clock():
    hr=time.strftime("%H")
    mins=time.strftime("%M")
    sec=time.strftime("%S")
    ap=time.strftime("%p")
    dat=time.strftime("%d")
    mon=time.strftime("%b")
    yrs=time.strftime("%Y")
    day=time.strftime("%A")
    clk.config(text=hr +":"+ mins +":"+ sec + ap)
    clk.after(1000,clock)
    datel.config(text=dat +"/"+ mon +"/"+ yrs)
    dayl.config(text=day)  
clk=Label(proj, text="", font=("Helvetica",10),bg='black',fg='red')
clk.place(relx=0.938,rely=0)
datel=Label(proj, text="", font=("Helvetica",10),bg='black',fg='red')
datel.place(relx=0.938,rely=0.03)
dayl=Label(proj, text="", font=("Helvetica",10),bg='black',fg='red')
dayl.place(relx=0.951,rely=0.06)
global datl
clock()

#-----------------------------------------------------------------------------------------------------------------
mydb = mc.connect(host='localhost',user='root',password='hari2561255')
cursor= mydb.cursor()
cursor.execute("create database if not exists railway")
mydb.commit()
mydb=mc.connect(host='localhost',user='root',password='hari2561255',database='railway')
cursor= mydb.cursor()
insert="create table if not exists customer(Firstname varchar(30),Lastname varchar(30),Gender varchar(30),Phoneno varchar(11),Tkt_No int(6),Date_of_Travel varchar(30),From_ varchar(30),To_ varchar(30),No_of_Tkts int,Fare float(8,3))"
cursor.execute(insert)
cursor.execute('show tables;')
data=cursor.fetchall()

#-----------------------------------------EXIT----------------------------------------------------------------------
def exit():
    proj.destroy()

#-------------------------------------------------TICKET---------------------------------------------------------------------
def ticket():
    f=bfn.get()
    l=bln.get()
    nam=f,'_',l
    p=bfn1.get()
    g=gnf.get()
    d1=dm.get()
    d2=int(d1)
    m1=mm.get()
    m2=int(m1)
    y1=dy.get()
    y2=int(y1)
    dte=d2,'/',m2,'/',y2
    fr=list1.get()
    to=list2.get()
    nft=nott.get()
    
    ftkt=Frame(proj,width=600,height=300,relief='sunken',bg='azure3',bd=5)
    ftkt.place(relx=0.4,rely=0.1)
    kf=Label(ftkt,text="----------------------------------TICKET------------------------------------------------------------------",font='kaiti')
    kf.place(relx=0,rely=0)
    
    tname=Label(ftkt,text="NAME :",bg='azure3',font='kaiti')
    tname.place(relx=0.1,rely=0.15)
    etname=Label(ftkt,width=15,bg='azure3',font='kaiti')
    etname['text']=nam
    etname.place(relx=0.20,rely=0.15,relwidth=0.3)

    global tktno
    tktno=random.randint(10000,99999)
    tkno=Label(ftkt,text="TICKET No.:",bg='azure3',font='kaiti')
    tkno.place(relx=0.6,rely=0.15)
    etkno=Label(ftkt,width=10,bg='azure3',font='kaiti')
    etkno['text']=tktno
    etkno.place(relx=0.75,rely=0.15)

    tkgn=Label(ftkt,text="GENDER :",bg='azure3',font='kaiti')
    tkgn.place(relx=0.1,rely=0.25)
    etkgn=Label(ftkt,width=10,bg='azure3',font='kaiti')
    etkgn['text']=g
    etkgn.place(relx=0.22,rely=0.25)

    tkfrm=Label(ftkt,text="FROM :",bg='azure3',font='kaiti')
    tkfrm.place(relx=0.1,rely=0.35)
    etkfrm=Label(ftkt,width=10,bg='azure3',font='kaiti')
    etkfrm['text']=fr
    etkfrm.place(relx=0.2,rely=0.35)

    tkto=Label(ftkt,text="TO :",bg='azure3',font='kaiti')
    tkto.place(relx=0.6,rely=0.35)
    etkto=Label(ftkt,width=10,bg='azure3',font='kaiti')
    etkto['text']=to
    etkto.place(relx=0.7,rely=0.35)

    tknot=Label(ftkt,text="NO. OF TKTS :",bg='azure3',font='kaiti')
    tknot.place(relx=0.1,rely=0.45)
    etknot=Label(ftkt,width=10,bg='azure3',font='kaiti')
    etknot['text']=nft
    etknot.place(relx=0.28,rely=0.45)

    plat=random.randint(1,4)
    tkpla=Label(ftkt,text="PLATFORM :",bg='azure3',font='kaiti')
    tkpla.place(relx=0.6,rely=0.45)
    etkpla=Label(ftkt,width=10,bg='azure3',font='kaiti')
    etkpla['text']=plat
    etkpla.place(relx=0.75,rely=0.45)

    tkdot=Label(ftkt,text="DATE OF TRAVEL :",bg='azure3',font='kaiti')
    tkdot.place(relx=0.25,rely=0.55)
    etkdot=Label(ftkt,width=15,bg='azure3',font='kaiti')
    etkdot['text']=dte
    etkdot.place(relx=0.48,rely=0.55)

    tkno=Label(ftkt,text="TOTAL FARE :",bg='azure3',font='kaiti')
    tkno.place(relx=0.25,rely=0.65)
    etkno=Label(ftkt,width=10,bg='azure3',font='kaiti')
    etkno['text']=ta
    etkno.place(relx=0.45,rely=0.65)

    tkjr=Label(ftkt,text="HAVE A SAFE AND HAPPY JOURNEY   :))",fg='red',font='kaiti')
    tkjr.place(relx=0.3,rely=0.75)

    koduf=Label(ftkt,text="-------------------------------------------------------------------------------------------------------------------------")
    koduf.place(relx=0,rely=0.92)
    
    fin=Button(proj, text='FINISH',font=('bauhaus93',13), bd=7 ,command=details,bg='cyan3',fg='orangered',)
    fin.place(relx=0.80,rely=0.6,relheight=0.05,relwidth=0.10)
    
#------------------------------------------CAL FARE---------------------------------------------------------------------
def cfare():
    Dp = list1.get()
    Ari = list2.get()
    nk=nott.get()
    Notic = int(nk)
    if (Dp == Ari):
        price=0.0*Notic
    elif (Dp,Ari) == ('Chromepet','Sanatorium') or (Dp,Ari) == ('Sanatorium','Chromepet') or (Dp,Ari) == ('Sanatorium','Tambaram') or (Dp,Ari) == ('Tambaram','Sanatorium') or (Dp,Ari) == ('Tambaram','Perungalathur') or (Dp,Ari) == ('Perungalathur','Tambaram'):
        price=5.0*Notic
    elif (Dp,Ari) == ('Chromepet','Pallavaram') or (Dp,Ari) == ('Pallavaram','Chromepet') or (Dp,Ari) == ('Pallavaram','Tirusulam') or (Dp,Ari) == ('Tirusulam','Pallavaram') or (Dp,Ari) == ('Tirusulam','Meenambakkam') or (Dp,Ari) == ('Meenambakkam','Tirusulam'):
        price=5.0*Notic
    elif (Dp,Ari) == ('Perungalathur','Sanatorium') or (Dp,Ari) == ('Sanatorium','Perungalathur') or (Dp,Ari) == ('Tambaram','Chromepet') or (Dp,Ari) == ('Chromepet','Tambaram') or (Dp,Ari) == ('Pallavaram','Sanatorium') or (Dp,Ari) == ('Sanatorium','Pallavaram'):
        price=10.0*Notic
    elif (Dp,Ari) == ('Chromepet','Tirusulam') or (Dp,Ari) == ('Tirusulam','Chromepet') or (Dp,Ari) == ('Pallavaram','Meenambakkam') or (Dp,Ari) == ('Meenambakkam','Pallavaram'):
        price=10.0*Notic
    elif (Dp,Ari) == ('Perungalathur','Chromepet') or (Dp,Ari) == ('Chromepet','Perungalathur') or (Dp,Ari) == ('Tambaram','Pallavaram') or (Dp,Ari) == ('Pallavaram','Tambaram'):
        price=15.0*Notic
    elif (Dp,Ari) == ('Sanatorium','Tirusulam') or (Dp,Ari) == ('Tirusulam','Sanatorium') or (Dp,Ari) == ('Chromepet','Meenambakkam') or (Dp,Ari) == ('Meenambakkam','Chromepet'):
        price=15.0*Notic
    elif (Dp,Ari) == ('Perungalathur','Pallavaram') or (Dp,Ari) == ('Pallavaram','Perungalathur') or (Dp,Ari) == ('Tambaram','Tirusulam') or (Dp,Ari) == ('Tirusulam','Tambaram') or (Dp,Ari) == ('Sanatorium','Meenambakkam') or (Dp,Ari) == ('Meenambakkam','Sanatorium'):
        price=20.0*Notic
    elif (Dp,Ari) == ('Perungalathur','Tirusulam') or (Dp,Ari) == ('Tirusulam','Perungalathur') or (Dp,Ari) == ('Tambaram','Meenambakkam') or (Dp,Ari) == ('Meenambakkam','Tambaram'):
        price=25.0*Notic
    elif (Dp,Ari) == ('Perungalathur','Meenambakkam') or (Dp,Ari) == ('Meenambakkam','Perungalathur'):
        price=30.0*Notic
    global ta
    ta=price
    global tf
    tf = Label(proj, text="Total Fare : ", font='bauhaus93',bg='steel blue',fg='snow',relief='raised',bd=4)
    tf.place(relx=0.02,rely=0.6,relheight=0.04,relwidth=0.11)
    global btf
    btf = Label(proj,font=('bauhaus93',13), width=6,bg='skyblue2',fg='snow',relief='raised',bd=4)
    btf['text']= '₹',price 
    btf.place(relx=0.15,rely=0.6,relheight=0.04,relwidth=0.10)
    global fin
    fin=Button(proj, text='PRINT TICKET', bd=7 ,bg='saddlebrown',fg='goldenrod3' ,command=ticket)
    fin.place(relx=0.15,rely=0.67,relheight=0.04,relwidth=0.15)
#-----------------------------------------------------------------------------------------------------------------
def details():
    f=bfn.get()
    l=bln.get()
    p=bfn1.get()
    g=gnf.get()
    d1=dm.get()
    d2=int(d1)
    m1=mm.get()
    m2=int(m1)
    y1=dy.get()
    y2=int(y1)
    n=datetime.date(y2,m2,d2)
    fr=list1.get()
    to=list2.get()
    nft=nott.get()
    insert="insert into customer(Firstname, Lastname, Gender, Phoneno, Tkt_No, Date_of_Travel, From_, To_, No_of_Tkts, Fare) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    record=(f,l,g,p,tktno,n,fr,to,nft,ta)
    cursor.execute(insert,record)
    mydb.commit()
    
    bfn.delete(first=0,last=100)
    bln.delete(first=0,last=100)
    bfn1.delete(first=0,last=100)
    gnf.delete(first=0,last=100)
    dm.delete(first=0,last=100)
    mm.delete(first=0,last=100)
    dy.delete(first=0,last=100)
    list1.delete(first=0,last=100)
    list2.delete(first=0,last=100)
    nott.delete(first=0,last=100)
    tf.destroy()
    btf.destroy()
    fin.destroy()
    lab=Label(proj,text='Thank you for choosing TrainMachan.com ;)', font='bauhaus93',bg='grey75',fg='magenta2',bd=5,relief='raised')
    lab.place(relx=0.4,rely=0.7,relheight=0.06,relwidth=0.3)

#-----------------------------------------------------------------------------------------------------------------
wel=Label(proj,text='Train Ticket Booking',font='castellar',bg='orange',fg='navy',relief='raised',bd=4)
wel.place(relx=0.2,rely=0.02,relheight=0.05,relwidth=0.5)
    
    
fn = Label(proj, text="First Name:", font='bauhaus93',bg='steel blue',fg='snow',relief='raised',bd=4)
fn.place(relx=0.02,rely=0.1,relheight=0.04,relwidth=0.12)
bfn = Entry(proj)
bfn.place(relx=0.15,rely=0.1,relheight=0.04,relwidth=0.15)

ln = Label(proj, text="Last Name:", font='bauhaus93',bg='steel blue',fg='snow',relief='raised',bd=4)
ln.place(relx=0.02,rely=0.15,relheight=0.04,relwidth=0.12)
bln = Entry(proj)
bln.place(relx=0.15,rely=0.15,relheight=0.04,relwidth=0.15)

gen=['Male','Female','Transgender']
gn = Label(proj, text="Gender : ", font='bauhaus93',bg='steel blue',fg='snow',relief='raised',bd=4)
gn.place(relx=0.02,rely=0.2,relheight=0.04,relwidth=0.12)
gnf=ttk.Combobox(proj,value=gen)
gnf.place(relx=0.15,rely=0.2,relheight=0.04,relwidth=0.15)

fn3 = Label(proj, text="Phone No. : ", font='bauhaus93',bg='steel blue',fg='snow',relief='raised',bd=4)
fn3.place(relx=0.02,rely=0.25,relheight=0.04,relwidth=0.12)
bfn1 = Entry(proj)
bfn1.place(relx=0.15,rely=0.25,relheight=0.04,relwidth=0.15)

date = Label(proj, text="Date of Travel:", font='bauhaus93',bg='steel blue',fg='snow',relief='raised',bd=4)
date.place(relx=0.02,rely=0.3,relheight=0.04,relwidth=0.12)
d=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
dm=ttk.Combobox(proj,values=d)
dm.place(relx=0.15,rely=0.3,relheight=0.04,relwidth=0.04)

m=[1,2,3,4,5,6,7,8,9,10,11,12]
mm=ttk.Combobox(proj,value=m)
mm.place(relx=0.2,rely=0.3,relheight=0.04,relwidth=0.04)

y=[2021,2022,2023]
dy=ttk.Combobox(proj,values=y)
dy.place(relx=0.25,rely=0.3,relheight=0.04,relwidth=0.04)

fr = Label(proj, text="FROM : ", font='bauhaus93',bg='steel blue',fg='snow',relief='raised',bd=4)
fr.place(relx=0.02,rely=0.35,relheight=0.04,relwidth=0.12)

station=['Perungalathur','Tambaram','Sanatorium','Chromepet','Pallavaram','Tirusulam','Meenambakkam']
list1=ttk.Combobox(proj,value=station)
list1.place(relx=0.15,rely=0.35,relheight=0.04,relwidth=0.15)

to = Label(proj, text="TO : ", font='bauhaus93',bg='steel blue',fg='snow',relief='raised',bd=4)
to.place(relx=0.02,rely=0.4,relheight=0.04,relwidth=0.12)

station1=['Perungalathur','Tambaram','Sanatorium','Chromepet','Pallavaram','Tirusulam','Meenambakkam']
list2=ttk.Combobox(proj,values=station1)
list2.place(relx=0.15,rely=0.4,relheight=0.04,relwidth=0.15)

no = Label(proj, text="No. of Tickets:", font='bauhaus93',bg='steel blue',fg='snow',relief='raised',bd=4)
no.place(relx=0.02,rely=0.45,relheight=0.04,relwidth=0.12)

nt=[1,2,3,4,5]
nott=ttk.Combobox(proj,value=nt)
nott.place(relx=0.15,rely=0.45,relheight=0.04,relwidth=0.15)

cf=Button(proj, text='Calculate Fare',font=('bauhaus93',12),bd=7, command=cfare,bg='aquamarine',fg='mediumpurple3',relief='raised')
cf.place(relx=0.15,rely=0.5,relheight=0.05,relwidth=0.15)

ex=Button(proj, text='Exit', bd=7, command=exit, bg='red',fg='black')
ex.place(relx=0.85,rely=0.75,relheight=0.06,relwidth=0.05)






