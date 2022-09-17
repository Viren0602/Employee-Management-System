from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def f1():
	mw.withdraw()
	aw.deiconify()

def f2():
	aw.withdraw()
	mw.deiconify()

def f3():
	mw.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0 , END)
	con = None
	try:
		con = connect("kc.db") 
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + " rno " + str(d[0]) + " name " + str(d[1]) + "\n"
		vw_st_data.insert(INSERT , info)

	except Exception as e:
		showerror("Galat Kiya" , e)
	finally :
		
		if con is not None:
			con.close()


def f4():
	vw.withdraw()
	mw.deiconify()

def f5():
	con = None
	try:
		con = connect("kc.db") 
		cursor = con.cursor()
		sql = "insert into student values('%d' , '%s')"
		rno = int(aw_ent_rno.get())
		name = aw_ent_name.get()
		if not(name.isalpha()):
			raise Exception("name shud contain only letters")
		cursor.execute(sql % (rno , name))
		con.commit()
		showinfo("Success" , "record added")

	except Exception as e:
		showerror("Galat Kiya" , e)
	finally :
		aw_ent_rno.delete(0 , END)
		aw_ent_name.delete(0 , END)
		aw_ent_rno.focus()
		if con is not None:
			con.close()

mw = Tk()
mw.title("S.M.S")
mw.geometry("600x600+50+50")

f = ("Arial" , 30 , "bold")
y = 20
mw_btn_add = Button(mw , text = "Add Student" , font = f , width = 15 , command = f1)
mw_btn_view = Button(mw , text = "View" , font = f , width = 15 , command = f3)
mw_btn_add.pack(pady = y)
mw_btn_view.pack(pady = y)

aw = Toplevel(mw)
aw.title("Add Student")
aw.geometry("600x600+50+50")

aw_lab_rno = Label(aw , text = "enter rno" , font = f)
aw_ent_rno = Entry(aw , font = f)
aw_lab_name = Label(aw , text = "enter name" , font = f)
aw_ent_name = Entry(aw , font = f)
aw_btn_save = Button(aw , text = "Save" , font = f , width = 15 , command = f5)
aw_btn_back = Button(aw , text = "Back" , font = f , width = 15 , command = f2)

aw_lab_rno.pack(pady = y)
aw_ent_rno.pack(pady = y)
aw_lab_name.pack(pady = y)
aw_ent_name.pack(pady = y)
aw_btn_save.pack(pady = y)
aw_btn_back .pack(pady = y)
aw.withdraw()

vw = Toplevel(mw)
vw.title("View Student")
vw.geometry("600x600+50+50")

vw_st_data = ScrolledText(vw , width = 20 , height = 8 , font = f)
vw_btn_back = Button(vw , text = "Back" , font = f , command = f4)
vw_st_data.pack(pady = y)
vw_btn_back.pack(pady = y)
vw.withdraw()

def confirmExit():
	if askokcancel('Jaa Rahe ho' , 'tussi jaa rahe ho?'):
		mw.destroy()
mw.protocol('WM_DELETE_WINDOW' , confirmExit)

mw.mainloop()






