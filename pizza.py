from sqlite3 import *
from tkinter import *
from tkinter import messagebox
class Login:
    pizzalist=[("Margherita",100,150,200,"1.png"),("Double Cheese",150,200,250,"2.png"),("Paneer Fest",175,225,275,"3.png"),("Italian Supreme",250,300,350,"4.png"),("Country Feast",300,350,400,"5.png"),("Exotic Supreme",500,550,600,"6.png"),
 ("Spicy Chicken",350,400,450,"7.png"),("Chickeroni",400,450,500,"8.png"),("Chicken Tikka",450,500,550,"9.png"),("Chicken Supremo",500,550,600,"10.png"),("Chicken Italian",600,650,700,"11.png"),("Chicken Exotica",700,750,800,"12.png"),
 ("Coca-Cola",40,60,80,"19.png"),("Thumbs Up",40,60,80,"20.png"),("Pepsi",40,60,80,"21.png"),("Mirinda",40,60,80,"22.png"),("7-UP",40,60,80,"23.png"),("Fanta",40,60,80,"24.png")]
    cart=[]
    def __init__(sf):
        sf.c=connect("mydata.db")
        sf.cur=sf.c.cursor()
        try:
            sf.cur.execute("create table staff(user varchar(50),passw varchar(50))")
        except:
            pass
        sf.scr=Tk(className="Pizza Management System")
        sf.scr.geometry("1350x750+0+0")
        sf.f1=Frame(sf.scr,bg="blue")
        sf.f1.pack(fill=BOTH,expand=1)
        img=PhotoImage(file="pizza1.png")
        sf.bg1=Label(sf.f1,image=img)
        sf.bg1.place(x=0,y=0,relwidth=1,relheight=1)
        sf.f=Frame(sf.f1,bg="blue")
        sf.f.pack(expand=1)
        sf.l=Label(sf.f,bg='black',fg='orange',font=('times',20,'bold'),text='user name')
        sf.l.grid(row=1,column=0)
        sf.user=Entry(sf.f,bg='black',fg='white',font=('times',20,'bold'))
        sf.user.grid(row=1,column=1)
        sf.l1=Label(sf.f,bg='black',fg='orange',font=('times',20,'bold'),text='password')
        sf.l1.grid(row=2,column=0)
        sf.passw=Entry(sf.f,bg='black',fg='white',font=('times',20,'bold'),show='*')
        sf.passw.grid(row=2,column=1)
        sf.b=Button(sf.f,text="submit",bg='black',fg='orange',font=('times',20,'bold'),command=lambda :sf.result("login"))
        sf.b.grid(row=3,column=0)
        sf.b1=Button(sf.f,text="register",bg='black',fg='orange',font=('times',20,'bold'),command=sf.register)
        sf.b1.grid(row=3,column=1)
        sf.scr.mainloop()
    def register(sf):
        try:
            sf.scr.destroy()
        except:
            try:
                sf.scr1.destroy()
            except:
                pass
        sf.scr1=Tk(className="Pizza Management System Register")
        sf.scr1.geometry("1350x750+0+0")
        sf.f1=Frame(sf.scr1,bg="blue",height=500,width=500)
        sf.f1.pack(fill=BOTH,expand=1)
        img=PhotoImage(file="pizza1.png")
        sf.bg1=Label(sf.f1,image=img)
        sf.bg1.place(x=0,y=0,relwidth=1,relheight=1)
        sf.f=Frame(sf.f1,bg="blue")
        sf.f.pack(expand=1)
        sf.l=Label(sf.f,bg='black',fg='orange',font=('times',20,'bold'),text='user name')
        sf.l.grid(row=1,column=0)
        sf.user=Entry(sf.f,bg='black',fg='white',font=('times',20,'bold'))
        sf.user.grid(row=1,column=1)
        sf.l1=Label(sf.f,bg='black',fg='orange',font=('times',20,'bold'),text='password')
        sf.l1.grid(row=2,column=0)
        sf.passw=Entry(sf.f,bg='black',fg='white',font=('times',20,'bold'),show='*')
        sf.passw.grid(row=2,column=1)
        sf.l2=Label(sf.f,bg='black',fg='orange',font=('times',20,'bold'),text='retype password')
        sf.l2.grid(row=3,column=0)
        sf.passw1=Entry(sf.f,bg='black',fg='white',font=('times',20,'bold'),show='*')
        sf.passw1.grid(row=3,column=1)
        sf.b=Button(sf.f,text="submit",bg='black',fg='orange',font=('times',20,'bold'),command=lambda :sf.result("register"))
        sf.b.grid(row=4,column=0)
        sf.b1=Button(sf.f,text="clear",bg='black',fg='orange',font=('times',20,'bold'))
        sf.b1.grid(row=4,column=1)
        sf.scr1.mainloop()
    def result(sf,val):
        if val=="login":
            try:
                sf.username=sf.user.get()
                sf.passd=sf.passw.get()
                sf.scr.destroy()
                x=sf.cur.execute("select count(*) from staff where user=%r and passw=%r"%(sf.username,sf.passd))
                if list(x)[0][0]==0:
                    messagebox.showinfo("Error","Incorrect username or password")
                    sf.__init__()
                else:
                    sf.mainmenu()
            except:
                pass
        elif val=='register':
            if sf.passw.get()==sf.passw1.get():
                x=sf.cur.execute("select count(*) from staff where user=%r"%(sf.user.get()))
                if list(x)[0][0]!=0:
                    messagebox.showinfo("pizza","username allready exists")
                    sf.register()
                else:
                    sf.cur.execute("insert into staff values(%r,%r)"%(sf.user.get(),sf.passw.get()))
                    sf.c.commit()
                try:
                    sf.scr1.destroy()
                except:
                    pass
                sf.__init__()
            else:
                try:
                    sf.scr1.destroy()
                except:
                    pass
                sf.register()
    def mainmenu(sf):
        sf.scr_m1=Tk(className="Main Menu")
        sf.scr_m1.geometry("1350x750+0+0")
        sf.f2=Frame(sf.scr_m1,bg="white")
        sf.f2.pack(fill=BOTH,expand=1)
        sf.img=PhotoImage(file="pizza1.png")
        sf.l_m1=Label(sf.f2,image=sf.img)
        sf.l_m1.place(x=0,y=0,relwidth=1,relheight=1)
        sf.imgg=PhotoImage(file="express.png")
        sf.l2=Label(sf.f2,image=sf.imgg)
        sf.l2.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l2.pack()
        sf.f=Frame(sf.f2,bg="red")
        sf.img_m1=PhotoImage(file="pizza2.png")
        sf.l_m1=Label(sf.f,image=sf.img_m1)
        sf.l_m1.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l_m1.grid(row=1,column=1)
        sf.b=Button(sf.f,text="Menu",font=('times',20,'bold'),command=lambda :sf.pizza())
        sf.b.grid(row=2,column=1)
        sf.img_m2=PhotoImage(file="cart.png")
        sf.l_m2=Label(sf.f,image=sf.img_m2)
        sf.l_m2.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l_m2.grid(row=1,column=3)
        sf.b2=Button(sf.f,text="Mycart",font=('times',20,'bold'),command=lambda :sf.finalbill())
        sf.b2.grid(row=2,column=3)
        sf.img_m3=PhotoImage(file="contact1.png")
        sf.l_m3=Label(sf.f,image=sf.img_m3)
        sf.l_m3.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l_m3.grid(row=1,column=4)
        sf.b3=Button(sf.f,text="CONTACT US",font=('times',20,'bold'),command=lambda :sf.contact())
        sf.b3.grid(row=2,column=4)
        sf.f.pack()
        sf.scr_m1.mainloop()
    def pizza(sf):
        sf.scr_m1.destroy()
        sf.scr_p=Tk(className="Pizza Menu")
        sf.scr_p.geometry("1350x750+0+0")
        sf.f=Frame(sf.scr_p,bg="white")
        sf.f.pack(fill=BOTH,expand=1)
        sf.img=PhotoImage(file="pizza1.png")
        sf.l_p1=Label(sf.f,image=sf.img)
        sf.l_p1.place(x=0,y=0,relwidth=1,relheight=1)
        sf.f2=Frame(sf.f,bg="white")
        sf.f2.pack()
        sf.img_m2=PhotoImage(file="express.png")
        sf.l_m2=Label(sf.f2,image=sf.img_m2)
        sf.l_m2.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l_m2.grid(row=1,column=2)
        sf.img_m1=PhotoImage(file="pizza2.png")
        sf.l_m1=Label(sf.f2,image=sf.img_m1)
        sf.l_m1.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l_m1.grid(row=2,column=1)
        sf.b=Button(sf.f2,text="veg-pizzas",font=('times',20,'bold'),command=lambda :sf.veg())
        sf.b.grid(row=3,column=1)
        sf.img_m3=PhotoImage(file="non2.png")
        sf.l_m2=Label(sf.f2,image=sf.img_m3)
        sf.l_m2.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l_m2.grid(row=2,column=3)
        sf.b2=Button(sf.f2,text="NON veg",font=('times',20,'bold'),command=lambda :sf.non())
        sf.b2.grid(row=3,column=3)
        sf.l=Label(sf.f2,text="choose your pizza",fg="black",font=("default",20))
        sf.img_m4=PhotoImage(file="cold.png")
        sf.l_m4=Label(sf.f2,image=sf.img_m4)
        sf.l_m4.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l_m4.grid(row=2,column=2)
        sf.b4=Button(sf.f2,text="Soft drinks",font=('times',20,'bold'),command=lambda :sf.drink())
        sf.b4.grid(row=3,column=2)
        sf.scr_p.mainloop()
    def veg(sf):
        sf.scr_p.destroy()
        sf.scr_v=Tk(className="veg Pizza ")
        sf.scr_v.geometry("1350x750+0+0")
        sf.f1=Frame(sf.scr_v,bg="white")
        sf.lab=Label(sf.scr_v,text="choose",fg="black",height=5)
        sf.lab.pack(fill=X)
        sf.l=Label(sf.f1,text="Margherita",fg="black")
        sf.l.grid(row=1,column=1)
        sf.img=PhotoImage(file="cart2.png")
        sf.img1=PhotoImage(file="1.png")
        sf.img2=PhotoImage(file="2.png")
        sf.img3=PhotoImage(file="3.png")
        sf.img4=PhotoImage(file="4.png")
        sf.img5=PhotoImage(file="5.png")
        sf.img6=PhotoImage(file="6.png")
        sf.l2=Label(sf.f1,image=sf.img1)
        sf.l2.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l2.grid(row=2,column=1,padx=10,pady=10)
        sf.l3=Label(sf.f1,text="Double cheese",fg="black")
        sf.l3.grid(row=1,column=2,padx=10,pady=10)
        sf.l4=Label(sf.f1,image=sf.img2)
        sf.l4.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l4.grid(row=2,column=2)
        sf.l5=Label(sf.f1,text="Paneer Fest",fg="black")
        sf.l5.grid(row=1,column=3)
        sf.l5=Label(sf.f1,image=sf.img3)
        sf.l5.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l5.grid(row=2,column=3)
        sf.lab2=Label(sf.f1,text="",fg="black",height=2)
        sf.lab2.grid(row=4,column=1)
        sf.l6=Label(sf.f1,text="Italian supreme",fg="black")
        sf.l6.grid(row=5,column=1)
        sf.l6=Label(sf.f1,image=sf.img4)
        sf.l6.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l6.grid(row=6,column=1)
        sf.l7=Label(sf.f1,text="Country Fest",fg="black")
        sf.l7.grid(row=5,column=2)
        sf.l7=Label(sf.f1,image=sf.img5)
        sf.l7.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l7.grid(row=6,column=2)
        sf.l8=Label(sf.f1,text="Exotic Supreme",fg="black")
        sf.l8.grid(row=5,column=3)
        sf.l8=Label(sf.f1,image=sf.img6)
        sf.l8.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l8.grid(row=6,column=3)
        sf.b1=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(1,1))
        sf.b1.grid(row=3,column=1)
        sf.b2=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(2,1))
        sf.b2.grid(row=3,column=2)
        sf.b3=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(3,1))
        sf.b3.grid(row=3,column=3)
        sf.b4=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(4,1))
        sf.b4.grid(row=7,column=1)
        sf.b5=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(5,1))
        sf.b5.grid(row=7,column=2)
        sf.b6=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(6,1))
        sf.b6.grid(row=7,column=3)
        
        sf.f1.pack()
        
        #sf.l.pack()
        #sf.l2.pack()
        sf.scr_v.mainloop()
    def non(sf):
        sf.scr_p.destroy()
        sf.scr_n=Tk(className="NoN Veg Pizza")
        sf.scr_n.geometry("1350x750+0+0")
        sf.f1=Frame(sf.scr_n,bg="white")
        sf.lab=Label(sf.scr_n,text="choose",fg="black",height=5)
        sf.lab.pack(fill=X)
        sf.l=Label(sf.f1,text="Spicy Chicken",fg="black")
        sf.l.grid(row=1,column=1)
        sf.img7=PhotoImage(file="7.png")
        sf.img8=PhotoImage(file="8.png")
        sf.img9=PhotoImage(file="9.png")
        sf.img10=PhotoImage(file="10.png")
        sf.img11=PhotoImage(file="11.png")
        sf.img12=PhotoImage(file="12.png")
        sf.l2=Label(sf.f1,image=sf.img7)
        sf.l2.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l2.grid(row=2,column=1)
        sf.l3=Label(sf.f1,text="Chickeroni",fg="black")
        sf.l3.grid(row=1,column=2)
        sf.l4=Label(sf.f1,image=sf.img8)
        sf.l4.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l4.grid(row=2,column=2)
        sf.l5=Label(sf.f1,text="Chicken Tikka",fg="black")
        sf.l5.grid(row=1,column=3)
        sf.l5=Label(sf.f1,image=sf.img9)
        sf.l5.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l5.grid(row=2,column=3)
        sf.lab2=Label(sf.f1,text="",fg="black",height=2)
        sf.lab2.grid(row=4,column=9)
        sf.l6=Label(sf.f1,text="Chicken Supremo",fg="black")
        sf.l6.grid(row=5,column=1)
        sf.l6=Label(sf.f1,image=sf.img10)
        sf.l6.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l6.grid(row=6,column=1)
        sf.l7=Label(sf.f1,text="Chicken Italian",fg="black")
        sf.l7.grid(row=5,column=2)
        sf.l7=Label(sf.f1,image=sf.img11)
        sf.l7.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l7.grid(row=6,column=2)
        sf.l8=Label(sf.f1,text="Chicken Exotica",fg="black")
        sf.l8.grid(row=5,column=3)
        sf.l8=Label(sf.f1,image=sf.img12)
        sf.l8.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l8.grid(row=6,column=3)
        sf.b1=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(7,2))
        sf.b1.grid(row=3,column=1)
        sf.b2=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(8,2))
        sf.b2.grid(row=3,column=2)
        sf.b3=Button(sf.f1,text="Add to cart ",fg="black",command=lambda :sf.bill(9,2))
        sf.b3.grid(row=3,column=3)
        sf.b4=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(10,2))
        sf.b4.grid(row=7,column=1)
        sf.b5=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(11,2))
        sf.b5.grid(row=7,column=2)
        sf.b6=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(12,2))
        sf.b6.grid(row=7,column=3)
        
        sf.f1.pack()
        
        #sf.l.pack()
        #sf.l2.pack()
        sf.scr_n.mainloop()
    def drink(sf):
        sf.scr_p.destroy()
        sf.scr_d=Tk(className="drink menu")
        sf.scr_d.geometry("1350x750+0+0")
        sf.f1=Frame(sf.scr_d,bg="white")
        sf.lab=Label(sf.scr_d,text="choose",fg="black",height=5)
        sf.lab.pack(fill=X)
        sf.l=Label(sf.f1,text="Coca-Cola",fg="black")
        sf.l.grid(row=1,column=1)
        sf.img13=PhotoImage(file="19.png")
        sf.img14=PhotoImage(file="20.png")
        sf.img15=PhotoImage(file="21.png")
        sf.img16=PhotoImage(file="22.png")
        sf.img17=PhotoImage(file="23.png")
        sf.img18=PhotoImage(file="24.png")
        sf.l2=Label(sf.f1,image=sf.img13)
        sf.l2.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l2.grid(row=2,column=1)
        sf.l3=Label(sf.f1,text="Thumbs-up",fg="black")
        sf.l3.grid(row=1,column=2)
        sf.l4=Label(sf.f1,image=sf.img14)
        sf.l4.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l4.grid(row=2,column=2)
        sf.l5=Label(sf.f1,text="Pepsi",fg="black")
        sf.l5.grid(row=1,column=3)
        sf.l5=Label(sf.f1,image=sf.img15)
        sf.l5.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l5.grid(row=2,column=3)
        sf.lab2=Label(sf.f1,text="",fg="black",height=2)
        sf.lab2.grid(row=4,column=9)
        sf.l6=Label(sf.f1,text="Mirinda",fg="black")
        sf.l6.grid(row=5,column=1)
        sf.l6=Label(sf.f1,image=sf.img16)
        sf.l6.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l6.grid(row=6,column=1)
        sf.l7=Label(sf.f1,text="7 UP",fg="black")
        sf.l7.grid(row=5,column=2)
        sf.l7=Label(sf.f1,image=sf.img17)
        sf.l7.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l7.grid(row=6,column=2)
        sf.l8=Label(sf.f1,text="Fanta",fg="black")
        sf.l8.grid(row=5,column=3)
        sf.l8=Label(sf.f1,image=sf.img18)
        sf.l8.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.l8.grid(row=6,column=3)
        sf.b1=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(13,3))
        sf.b1.grid(row=3,column=1)
        sf.b2=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(14,3))
        sf.b2.grid(row=3,column=2)
        sf.b3=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(15,3))
        sf.b3.grid(row=3,column=3)
        sf.b4=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(16,3))
        sf.b4.grid(row=7,column=1)
        sf.b5=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(17,3))
        sf.b5.grid(row=7,column=2)
        sf.b6=Button(sf.f1,text="Add to cart",fg="black",command=lambda :sf.bill(18,3))
        sf.b6.grid(row=7,column=3)
        
        sf.f1.pack()
        
        #sf.l.pack()
        #sf.l2.pack()
        sf.scr_d.mainloop()
    def bill(sf,ch,close):
        if(close==1):
            sf.scr_v.destroy()
        else:
            pass
        if(close==2):
            sf.scr_n.destroy()
        else:
            pass
        if(close==3):
            sf.scr_d.destroy()
        else:
            pass
        sf.scr_q=Tk(className="Quantity and Size")
        sf.scr_q.geometry("1350x750+0+0")
        sf.f=Frame(sf.scr_q,bg="white")
        print(sf.pizzalist[ch-1])
        sf.img=PhotoImage(file=sf.pizzalist[ch-1][4])
        sf.l=Label(sf.f,image=sf.img)
        sf.l.place(x=0,y=0,relwidth=0.4,relheight=0.4)
        sf.f1=Frame(sf.scr_q,bg="white")
        sf.c4=Button(sf.f1,text="SIZE",font=('default',23))
        sf.c4.grid(row=0,column=1,padx=20,pady=20)
        sf.c5=Button(sf.f1,text="QUANTITY",font=('default',23))
        sf.c5.grid(row=0,column=2,padx=20,pady=20)
        sf.c1=Button(sf.f1,text="SMALL",font=('default',23))
        sf.c1.grid(row=1,column=1,padx=20,pady=20)
        sf.scale=Scale(sf.f1,from_=0,to=5,relief="raised",tickinterval=1,sliderlength=4,orient="horiz",resolution=1)
        sf.scale.grid(row=1,column=2)
        sf.c2=Button(sf.f1,text="MEDIUM",font=('default',23))
        sf.c2.grid(row=2,column=1,padx=20,pady=20)
        sf.scale2=Scale(sf.f1,from_=0,to=5,relief="raised",tickinterval=1,sliderlength=4,orient="horiz",resolution=1)
        sf.scale2.grid(row=2,column=2)
        sf.c3=Button(sf.f1,text="LARGE  ",font=('default',23))
        sf.c3.grid(row=3,column=1,padx=20,pady=20)
        sf.scale3=Scale(sf.f1,from_=0,to=5,relief="raised",tickinterval=1,sliderlength=4,orient="horiz",resolution=1)
        sf.scale3.grid(row=3,column=2)
        sf.c6=Button(sf.f1,text="CONFIRM",font=('default',23),command=lambda :sf.billup(ch,sf.scale.get(),sf.scale2.get(),sf.scale3.get()))
        sf.c6.grid(row=1,column=3,padx=20,pady=20)
        sf.c7=Button(sf.f1,text="BACK",font=('default',23))
        sf.c7.grid(row=2,column=3,padx=20,pady=20)
        sf.f.pack()
        sf.f1.pack()
        sf.l.pack()
        sf.scr_q.mainloop()
    def billup(sf,val,sqt,mqt,lqt):
        sf.scr_q.destroy()
        sf.el=sf.pizzalist[val-1]
        if(sqt>0):
            sf.c=(sf.el[0],"s",sf.el[1],sqt,(sqt*sf.el[1]))
            sf.cart.append(sf.c)
        else:
            pass
        if(mqt>0):
            sf.c2=(sf.el[0],"m",sf.el[2],mqt,(mqt*sf.el[2]))
            sf.cart.append(sf.c2)
        else:
            pass
        if(lqt>0):
            sf.c3=(sf.el[0],"l",sf.el[3],lqt,(lqt*sf.el[3]))
            sf.cart.append(sf.c3)
        else:
            pass
        print(sf.cart)
        sf.mainmenu()
    def finalbill(sf):
        sf.scr_m1.destroy()
        sf.scr5=Tk(className="bill")
        sf.scr5.geometry("1350x750+0+0")
        sf.scr5.configure(background='black')

        sf.t=Frame(sf.scr5, width=1350, height=100 ,bd=14,relief="raise")
        sf.t.pack(side=TOP)

        sf.f2=Frame(sf.scr5, width=1350, height=650 ,bd=8,relief="raise")
        sf.f2.pack(side=BOTTOM)

        sf.ft2=Frame(sf.f2, width=1350, height=450 ,bd=12,relief="raise")
        sf.ft2.pack(side=TOP)

        sf.fb2=Frame(sf.f2, width=1350, height=250 ,bd=16,relief="raise")
        sf.fb2.pack(side=BOTTOM)

        sf.l=Label(sf.t,font=('arial',50,'bold'),text="\tYour Bill                " ,bd=10)
        sf.l.grid(row=0,column=0)

        sf.l1=Label(sf.ft2,font=('arial',12,'bold'),text="Receipt",bd=2)
        sf.l1.grid(row=0,column=0,sticky=W)
        sf.tx1=Text(sf.ft2,width=99,height=22,bg="white",bd=8,font=('arial',11,'bold'))
        sf.tx1.grid(row=1,column=0)
#------------------------
        
        def pay():
            sf.pay=messagebox.askyesno("Thank you","Do you want to quit?")
            if sf.pay > 0:
                sf.rem()
                sf.cart.clear()
                
                sf.scr5.destroy()
                sf.mainmenu()
                return

        sf.cost=0
        sf.tax=0
        sf.tot=0
#----------------------------------
        sf.lsub=Label(sf.fb2,font=('arial',16,'bold'),text="Sub Total",bd=8)
        sf.lsub.grid(row=0,column=0)
        sf.txsub=Entry(sf.fb2,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left')
        sf.txsub.grid(row=0,column=1)

        sf.ltax=Label(sf.fb2,font=('arial',16,'bold'),text="Tax",bd=8)
        sf.ltax.grid(row=0,column=2)
        sf.txtax=Entry(sf.fb2,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left')
        sf.txtax.grid(row=0,column=3)

        sf.ltotal=Label(sf.fb2,font=('arial',16,'bold'),text="Total",bd=8)
        sf.ltotal.grid(row=0,column=4)
        sf.txtotal=Entry(sf.fb2,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left')
        sf.txtotal.grid(row=0,column=5)

        sf.bpay=Button(sf.fb2,padx=16,pady=1 ,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Pay",command=pay)
        sf.bpay.grid(row=0,column=6)
        sf.bhist=Button(sf.fb2,padx=16,pady=1 ,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="history",command=lambda :sf.history())
        sf.bhist.grid(row=1,column=6)
        sf.bdel=Button(sf.fb2,padx=16,pady=1 ,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="del item",command=lambda :sf.delete())
        sf.bdel.grid(row=1,column=4)


        sf.tx1.insert(END,'S.no\t'+'Items\t\t\t'+'size\t'+'Price\t\t'+'QTY\t'+'T.Price\n')
        sf.sl=1
        for i,j in enumerate(sf.cart):
            sf.tx1.insert(END,str(sf.sl)+'\t'+sf.cart[i][0]+'\t\t\t'+str(sf.cart[i][1])+'\t'+str(sf.cart[i][2])+'\t\t'+str(sf.cart[i][3])+'\t'+str(sf.cart[i][4])+'\n')
            sf.sl=sf.sl+1
            sf.cost+=sf.cart[i][4]

        sf.txsub.insert(END,str(sf.cost))
        sf.tax=(sf.cost*15)/100
        sf.txtax.insert(END,str(sf.tax))
        sf.tot=sf.cost+sf.tax
        sf.txtotal.insert(END,str(sf.tot))


        sf.scr5.mainloop()
    def history(sf):
        sf.rem()
        sf.scr5.destroy()
        sf.scrh=Tk(className="history")
        sf.scrh.geometry("1350x750+0+0")
        sf.scrh.configure(background='black')

        sf.t=Frame(sf.scrh, width=1350, height=100 ,bd=14,relief="raise")
        sf.t.pack(side=TOP)

        sf.f2=Frame(sf.scrh, width=1350, height=650 ,bd=8,relief="raise")
        sf.f2.pack(side=BOTTOM)

        sf.ft2=Frame(sf.f2, width=1350, height=450 ,bd=12,relief="raise")
        sf.ft2.pack(side=TOP)

        sf.fb2=Frame(sf.f2, width=1350, height=250 ,bd=16,relief="raise")
        sf.fb2.pack(side=BOTTOM)

        sf.l=Label(sf.t,font=('arial',70,'bold'),text="\tHISTORY                " ,bd=10)
        sf.l.grid(row=0,column=0)

        sf.l1=Label(sf.ft2,font=('arial',12,'bold'),text="Receipt",bd=2)
        sf.l1.grid(row=0,column=0,sticky=W)
        sf.tx1=Text(sf.ft2,width=99,height=22,bg="white",bd=8,font=('arial',11,'bold'))
        sf.tx1.grid(row=1,column=0)
        sf.bpay=Button(sf.fb2,padx=16,pady=1 ,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="back",command=lambda :sf.back())
        sf.bpay.grid(row=0,column=6)
        sf.tx1.insert(END,'Items\t\t\t\t\t'+'size\t'+'Price\t\t'+'QTY\t'+'T.Price\n')
        sf.file=open(sf.fname,'r')
        print(sf.file.readable())
        sf.file.seek(0)
        sf.hist=sf.file.read()    
        sf.tx1.insert(END,sf.hist)
        sf.scrh.mainloop()
    def back(sf):
        sf.scrh.destroy()
        sf.mainmenu()
    def delete(sf):
        sf.scr5.destroy()
        sf.scr_dl=Tk(className="remove item from cart")
        sf.scr_dl.geometry("1350x750+0+0")
        sf.scr_dl.configure(background='black')

        sf.t=Frame(sf.scr_dl, width=1350, height=100 ,bd=14,relief="raise")
        sf.t.pack(side=TOP)

        sf.f2=Frame(sf.scr_dl, width=1350, height=650 ,bd=8,relief="raise")
        sf.f2.pack(side=BOTTOM)

        sf.ft2=Frame(sf.f2, width=1350, height=450 ,bd=12,relief="raise")
        sf.ft2.pack(side=TOP)

        sf.fb2=Frame(sf.f2, width=1350, height=250 ,bd=16,relief="raise")
        sf.fb2.pack(side=BOTTOM)

        sf.l=Label(sf.t,font=('arial',50,'bold'),text="\tREMOVE ITEM                " ,bd=10)
        sf.l.grid(row=0,column=0)

        sf.l1=Label(sf.ft2,font=('arial',12,'bold'),text="Receipt",bd=2)
        sf.l1.grid(row=0,column=0,sticky=W)
        sf.tx1=Text(sf.ft2,width=99,height=22,bg="white",bd=8,font=('arial',11,'bold'))
        sf.tx1.grid(row=1,column=0)
        sf.bpay=Button(sf.fb2,padx=16,pady=1 ,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="delete item",command=lambda :sf.del_item(sf.delitemno.get()))
        sf.bpay.grid(row=0,column=6)
        sf.tx1.insert(END,'S.no\t'+'Items\t\t\t'+'size\t'+'Price\t\t'+'QTY\t'+'T.Price\n')
        sf.sl=0
        for i,j in enumerate(sf.cart):
            sf.tx1.insert(END,str(sf.sl)+'\t'+sf.cart[i][0]+'\t\t\t'+str(sf.cart[i][1])+'\t'+str(sf.cart[i][2])+'\t\t'+str(sf.cart[i][3])+'\t'+str(sf.cart[i][4])+'\n')
            sf.sl=sf.sl+1
        sf.lsub=Label(sf.fb2,font=('arial',16,'bold'),text="enter item no.",bd=8)
        sf.lsub.grid(row=0,column=0)
        sf.delitemno=Entry(sf.fb2,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left')
        sf.delitemno.grid(row=0,column=1)
        sf.scr_dl.mainloop()
    def del_item(sf,item):
        print(item)
        print("loop:")
        for i,j in enumerate(sf.cart):
            print(i)
            if(item==str(i)):
                print("a")
                print(sf.cart.pop(i))
            else:
                print('b')
        sf.scr_dl.destroy()
        sf.mainmenu()
    def rem(sf):
        sf.ext=".txt"
        sf.fname=sf.username+sf.ext
        sf.file=open(sf.fname,'a+')
        for i,j in enumerate(sf.cart):
            sf.hist=sf.cart[i][0]
            sf.hist2=sf.cart[i][1]
            sf.hist3=sf.cart[i][2]
            sf.hist4=sf.cart[i][3]
            sf.hist5=sf.cart[i][4]
            sf.file.writelines(sf.hist+"\t\t\t\t\t"+sf.hist2+"\t"+str(sf.hist3)+'\t\t'+str(sf.hist4)+'\t'+str(sf.hist5)+'\n')
        sf.file.close()
    def contact(sf):
        sf.scr_m1.destroy()
        sf.scr_c=Tk(className="Main Menu")
        sf.scr_c.geometry("1350x750+0+0")
        sf.f2=Frame(sf.scr_c,bg="white")
        sf.f2.pack(fill=BOTH,expand=1)
        sf.img=PhotoImage(file="piz1.png")
        sf.l_m1=Label(sf.f2,image=sf.img)
        sf.l_m1.place(x=0,y=0,relwidth=1,relheight=1)
        sf.scr_c.mainloop()

x=Login()
