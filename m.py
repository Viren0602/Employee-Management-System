from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def f1():				#ADD WINDOW
	mw.withdraw()
	aw.deiconify()

def f2():
	aw.withdraw()
	mw.deiconify()

def f3():				#VIEW WINDOW
	mw.withdraw()
	vw.deiconify()
	con = None
	vw_st_data.delete(1.0, END)
	try:
		con = connect("mahek.db")
		cursor = con.cursor()
		sql = "select * from  employee"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + " id " + str(d[0]) + " name " + str(d[1] + " salary " + str(d[2]) + "\n")
		vw_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("Error", e)
	finally:
		if con is not None:
			con.close()

def f4():
	vw.withdraw()
	mw.deiconify()

def f5():				#UPDATE WINDOW
	mw.withdraw()
	uw.deiconify()
	#con = None
	#try:
		#con = connect("kc.db")
		#cursor = con.cursor()
		#sql =	 "update employee set name = '%s', where id = '%d' , salary = '%f' "	     	 
		#cursor = con.cursor()
		#id = int(input("enter emp id "))	
		#name = input("enter emp  updated name ")
		#salary = float(input("enter salary"))
		#cursor.execute(sql % (name, id, salary))
		#if cursor.rowcount == 1:											
			#con.commit()																						
			#showinfo("Suceess", "record updated")
	#except Exception as e:
		#showwrror("Error", e)			 
	

def f6():
	uw.withdraw()
	mw.deiconify()

def f7():				#DELETE WINDOW
	mw.withdraw()
	dw.deiconify()

def f8():
	mw.deiconify()
	dw.withdraw()

def f9():				#DATABASE
	con = None
	try:
		con = connect("mahek.db")
		cursor = con.cursor()
		sql = "insert into employee values('%d', '%s', '%f')"
		id = int(aw_ent_id.get())
		name = aw_ent_name.get()
		salary = float(aw_ent_salary.get())
		cursor.execute(sql % (id, name, salary))
		con.commit()
		showinfo("Success", "record added")
	except Exception as e:
		showerror("Error", e)
	finally:
		aw_ent_id.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_salary.delete(0, END)
		aw_ent_id.focus()
		if con is not None:
			con.close()

		
		
	

	
	
mw = Tk()
mw.title("Employee Management System")
mw.geometry("600x700+50+50")

f = ("Arial", 30, "bold")
y = 12

#MAIN WINDOW
mw_btn_add = Button(mw, text = "Add Employee", font=f, width=15, command=f1)
mw_btn_view = Button(mw, text= "View Employee", font=f, width=15, command=f3)
mw_btn_update = Button(mw, text= "Update Employee", font=f, width=15, command=f5)
mw_btn_delete = Button(mw, text= "Delete Employee", font=f, width=15, command=f7)
mw_btn_add.pack(pady=y)
mw_btn_view.pack(pady=y)
mw_btn_update.pack(pady=y)
mw_btn_delete.pack(pady=y)


#ADD WINDOW
aw = Toplevel(mw)
aw.title("Add Employee")
aw.geometry("600x700+50+50")

aw_lab_id = Label(aw, text="enter id", font=f)
aw_ent_id = Entry(aw, font=f)
aw_lab_name = Label(aw, text="enter name", font=f)
aw_ent_name = Entry(aw, font=f)
aw_lab_salary = Label(aw, text="enter salary", font=f)
aw_ent_salary = Entry(aw, font=f)
aw_btn_save = Button(aw, text="Save", font=f, command=f9)
aw_lab_back = Button(aw, text="Back", font=f, command=f2)
aw_lab_id.pack(pady=y)
aw_ent_id.pack(pady=y)
aw_lab_name.pack(pady=y)
aw_ent_name.pack(pady=y)
aw_lab_salary.pack(pady=y)
aw_ent_salary.pack(pady=y)
aw_btn_save.pack(pady=y)
aw_lab_back.pack(pady=y)
aw.withdraw()



#VIEW WINDOW
vw = Toplevel(mw)
vw.title("View Employee")
vw.geometry("600x700+50+50")

vw_st_data = ScrolledText(vw, width=20, height=8, font=f)		
vw_st_data.pack(pady=y)
vw_btn_back = Button(vw, text="Back", font=f, command=f4)
vw_btn_back.pack(pady=y)
vw.withdraw()



#UPDATE WINDOW
uw = Toplevel(mw)
uw.title("Update Employee")
uw.geometry("600x700+50+50")

uw_lab_id = Label(uw, text="enter id", font=f)
uw_ent_id = Entry(uw, font=f)
uw_lab_name = Label(uw, text="enter name", font=f)
uw_ent_name = Entry(uw, font=f)
uw_lab_salary = Label(uw, text="enter salary", font=f)
uw_ent_salary = Entry(uw, font=f)
uw_btn_save = Button(uw, text="Save", font=f)
uw_lab_back = Button(uw, text="Back", font=f, command=f6)
uw_lab_id.pack(pady=y)
uw_ent_id.pack(pady=y)
uw_lab_name.pack(pady=y)
uw_ent_name.pack(pady=y)
uw_lab_salary.pack(pady=y)
uw_ent_salary.pack(pady=y)
uw_btn_save.pack(pady=y)
uw_lab_back.pack(pady=y)
uw.withdraw()



#DELETE WINDOW
dw = Toplevel(mw)
dw.title("Update Employee")
dw.geometry("600x700+50+50")

dw_lab_id = Label(dw, text="enter id", font=f)
dw_ent_id = Entry(dw, font=f)
dw_btn_save = Button(dw, text="Save", font=f)
dw_lab_back = Button(dw, text="Back", font=f, command=f8)
dw_lab_id.pack(pady=y)
dw_ent_id.pack(pady=y)
dw_btn_save.pack(pady=y)
dw_lab_back.pack(pady=y)
dw.withdraw()


def confirmExit():
	if askokcancel('Quit', 'Are u sure u want to exit'):
		mw.destroy()
mw.protocol('WM_DELETE_WINDOW', confirmExit)

mw.mainloop()