from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests
import re

def f1():
    mw.withdraw()
    aw.deiconify()

def f2():
    aw.withdraw()
    mw.deiconify()

def f3():
    mw.withdraw()
    vw.deiconify()
    vw_st_data.delete(1.0, END)
    con=None
    try:
        con=connect("kc.db")
        cursor=con.cursor()
        sql="select * from student"
        cursor.execute(sql)
        data=cursor.fetchall()
        info=""
        for d in data:
            info=info +" rno="+str(d[0])+" name= "+str(d[1])+" marks="+str(d[2])+"\n"
        vw_st_data.insert(INSERT,info)
    except Exception as e:
        showerror("Issue",e)
    finally:
        if con is not None:
            con.close()
def f4():
    vw.withdraw()
    mw.deiconify()

def f5():
    con=None
    try:
        con=connect("kc.db")
        cursor=con.cursor()
        sql="insert into student values('%d','%s','%d')"
        try:
            rno=int(aw_ent_rno.get())
            name=aw_ent_name.get()
            marks=int(aw_ent_marks.get())
            def validate_name(name):
                                pattern = "^[A-Za-zÀ-ÖØ-öø-ÿ '-]+$"
                                return bool(re.match(pattern, name))
            if rno<1:
                raise Exception("min rno should be 1")
            elif len(name)==0 or len(name)<2 and name.isalpha()==True:
                raise Exception("Name should not be blank or less than 2 characters")
            elif validate_name(name)==False:
                raise Exception("Name should contain alphabets")
            elif marks<0 or marks>100: 
                raise Exception("Marks should be between 0 to 100")
        except ValueError:
            showerror("Issue","Invalid input-It should not be blank and it should contain only integers")
            return
        except Exception as e:
            showerror("issue",e)
            return 
            
                

            
        cursor.execute(sql%(rno,name,marks))
        con.commit()
        showinfo("Success","info saved")
    except Exception as e:
        if type(e).__name__=="IntegrityError":
            showerror("Issue","rno already exists")
        else:
            showerror("issue",e)
    finally:
        if con is not None:
            con.close()
        aw_ent_rno.delete(0,END)
        aw_ent_name.delete(0,END)
        aw_ent_marks.delete(0,END)
        aw_ent_rno.focus()


def f6():
    mw.withdraw()
    uw.deiconify()

def f7():
    uw.withdraw()
    mw.deiconify()

def f8():
    con=None
    try:
        con=connect("kc.db")
        cursor=con.cursor()
        sql="update student set name='%s', marks='%d' where rno='%d' "
        try:
            rno=int(uw_ent_rno.get())
            name=uw_ent_name.get()
            marks=int(uw_ent_marks.get())
            def validate_name(name):
                                pattern = "^[A-Za-zÀ-ÖØ-öø-ÿ '-]+$"
                                return bool(re.match(pattern, name))
            if rno<1:
                raise Exception("min rno should be 1")
            if len(name)==0 or len(name)<2 and name.isalpha()==True:
                raise Exception("Name should not be blank or less than 2 characters")
            elif validate_name(name)==False:
                raise Exception("Name should contain alphabets")
            if marks<0 or marks>100:
                raise Exception("Marks should be between 0 to 100")
                
        except ValueError:
            showerror("Issue","Invalid input-It should not be blank and it should contain only integers")
            return
        except Exception as e:
            showerror("issue",e)
            return 
        
        cursor.execute(sql%(name,marks,rno))
        if cursor.rowcount==1:
            con.commit()
            showinfo("Success","record updated")
        else:
            showerror("Error","record does not exists")
    except Exception as e:
        if type(e).__name__=="IntegrityError":
            showerror("Issue","rno already exists")
        else:
            showerror("issue",e)
    finally:
        if con is not None:
            con.close()
        uw_ent_rno.delete(0,END)
        uw_ent_name.delete(0,END)
        uw_ent_marks.delete(0,END)
        uw_ent_rno.focus()

def f9():
    mw.withdraw()
    dw.deiconify()

def f10():
    dw.withdraw()
    mw.deiconify()

def f11():
    con=None
    try:
        con=connect("kc.db")
        cursor=con.cursor()
        sql="delete from student where rno='%d'"
        try:
            rno=int(dw_ent_rno.get())
            if rno<1:
                raise Exception("min rno should be 1")
                
        except ValueError:
            showerror("Issue","invalid rno")
            return
        except Exception as e:
            showerror("issue",e)
            return 
        cursor.execute(sql%(rno))
        if cursor.rowcount==1:
            con.commit()
            showinfo("Success","record deleted")
        else:
            showerror("Error","record does not exists")
    finally:
        if con is not None:
            con.close()
        dw_ent_rno.delete(0,END)
        dw_ent_rno.focus()


def f12():
    con=connect("kc.db")
    cursor=con.cursor()
    cursor.execute('SELECT name,marks FROM student ORDER BY marks DESC LIMIT 5')
    data = cursor.fetchall()

    name=[]
    marks=[]
    
    for row in data:
        name.append(row[0])
        marks.append(row[1])

    plt.bar(name,marks,width=0.3,color=["red","green","blue","pink","yellow"])
    plt.title("Top 5 Students")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.show()


def f13():
    try:
        wa="https://ipinfo.io/"
        res=requests.get(wa)
        data=res.json()
        city_name=data["city"]
        return city_name
    except Exception as e:
        showerror("issue",e)


def f14():
    try:
        a1="https://api.openweathermap.org/data/2.5/weather"
        a2="?q="+city
        a3="&appid="+"3445aed2afa10f1d43ddd2d6c89b053c"
        a4="&units="+"metric"
        wa=a1+a2+a3+a4
        res=requests.get(wa)
        data=res.json()
        temp=data["main"]["temp"]
        return temp
    
    except Exception as e:
        showerror("issue",e)

def f15():
    try:
    
        wa="http://api.quotable.io/random"
        res=requests.get(wa)
        #print(res)
        data=res.json()
        #print(data)
        msg=data["content"]
        return msg
    except Exception as e:
        showerror("issue",e)



mw=Tk()
mw.title("Student Management System")
mw.configure(bg='#dcd3f2')
mw.geometry("1920x1080+50+50")
f=("Simsun",30,"bold")

img= PhotoImage(file='image2.png', master= mw)
img_label= Label(mw,image=img)

img_label.place(x=0, y=0, relwidth=1, relheight=1)



city=str(f13())

mw_btn_add=Button(mw,text="Add Student",font=f,width=15,command=f1)
mw_btn_view=Button(mw,text="View Student",font=f,width=15,command=f3)
mw_btn_update=Button(mw,text="Update Student",font=f,width=15,command=f6)
mw_btn_delete=Button(mw,text="Delete Student",font=f,width=15,command=f9)
mw_btn_chart=Button(mw,text="Chart",font=f,width=15,command=f12)
mw_lab_loc=Label(mw,text="Loc=",font=f,bg='#dcd3f2')
mw_lab_temp=Label(mw,text="Temp=",font=f,bg='#dcd3f2')
mw_lab_quote=Label(mw,text="Quote=",font=f,bg='#dcd3f2',wraplength=1500)
mw_lab_loc.config(text=f13())
mw_lab_temp.config(text=f14())
mw.after(500, lambda: mw_lab_quote.config(text=''.join(f15())))



mw_btn_add.pack(pady=5)
mw_btn_view.pack(pady=5)
mw_btn_update.pack(pady=5)
mw_btn_delete.pack(pady=5)
mw_btn_chart.pack(pady=5)
mw_lab_loc.pack(pady=5)
mw_lab_temp.pack(pady=5)
mw_lab_quote.pack(pady=20)


mw_lab_loc.place(relx = 0.0,rely = 1.0,anchor ='sw')
mw_lab_temp.place(relx = 1.0,rely = 1.0,anchor ='se')





aw=Toplevel(mw)
aw.title("Add Student")
aw.geometry("1920x1080+50+50")
aw.configure(bg='#c1ddf7')

aw_lab_rno=Label(aw,text="enter rno",font=f,bg='#c1ddf7')
aw_ent_rno=Entry(aw,font=f)
aw_lab_name=Label(aw,text="enter name",font=f,bg='#c1ddf7')
aw_ent_name=Entry(aw,font=f)
aw_lab_marks=Label(aw,text="enter marks",font=f,bg='#c1ddf7')
aw_ent_marks=Entry(aw,font=f)
aw_btn_save=Button(aw,text="Save",font=f,command=f5)
aw_btn_back=Button(aw,text="Back",font=f,command=f2)

aw_lab_rno.pack(pady=5)
aw_ent_rno.pack(pady=5)
aw_lab_name.pack(pady=5)
aw_ent_name.pack(pady=5)
aw_lab_marks.pack(pady=5)
aw_ent_marks.pack(pady=5)
aw_btn_save.pack(pady=5)
aw_btn_back.pack(pady=5)
aw.withdraw()

vw=Toplevel(mw)
vw.title("View Student")
vw.geometry("1920x1080+50+50")
vw.configure(bg='#fff2cc')



vw_st_data=ScrolledText(vw,width=25,height=5,font=5,bg='#fff2cc')
vw_btn_back=Button(vw,text="Back",font=f,command=f4)

vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()


uw=Toplevel(mw)
uw.title("Update Student")
uw.geometry("1920x1080+50+50")
uw.configure(bg='#fbdbba')


uw_lab_rno=Label(uw,text="enter rno",font=f,bg='#fbdbba')
uw_ent_rno=Entry(uw,font=f)
uw_lab_name=Label(uw,text="enter new name",font=f,bg='#fbdbba')
uw_ent_name=Entry(uw,font=f)
uw_lab_marks=Label(uw,text="enter new marks",font=f,bg='#fbdbba')
uw_ent_marks=Entry(uw,font=f)
uw_btn_save=Button(uw,text="Update",font=f,command=f8)
uw_btn_back=Button(uw,text="Back",font=f,command=f7)

uw_lab_rno.pack(pady=5)
uw_ent_rno.pack(pady=5)
uw_lab_name.pack(pady=5)
uw_ent_name.pack(pady=5)
uw_lab_marks.pack(pady=5)
uw_ent_marks.pack(pady=5)
uw_btn_save.pack(pady=5)
uw_btn_back.pack(pady=5)
uw.withdraw()


dw=Toplevel(mw)
dw.title("Delete Student")
dw.geometry("1920x1080+50+50")
dw.configure(bg='#d9ead3')

dw_lab_rno=Label(dw,text="enter rno",font=f,bg='#d9ead3')
dw_ent_rno=Entry(dw,font=f)
dw_btn_delete=Button(dw,text="Delete",font=f,command=f11)
dw_btn_back=Button(dw,text="Back",font=f,command=f10)

dw_lab_rno.pack(pady=10)
dw_ent_rno.pack(pady=10)
dw_btn_delete.pack(pady=10)
dw_btn_back.pack(pady=10)
dw.withdraw()


def windowclose():
    if askyesnocancel("Quit","Are you sure, you want to exit?"):
                mw.destroy()
mw.protocol("WM_DELETE_WINDOW",windowclose)
aw.protocol("WM_DELETE_WINDOW",windowclose)
vw.protocol("WM_DELETE_WINDOW",windowclose)
uw.protocol("WM_DELETE_WINDOW",windowclose)
dw.protocol("WM_DELETE_WINDOW",windowclose)

mw.mainloop()