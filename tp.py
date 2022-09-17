from tkinter import * 
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
#from PIL import ImageTk, Image
from PIL import Image, ImageTk

def f1():
	mw.withdraw()
	aw.deiconify()
def f2():
	mw.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0 , END)
	con = None
	try:
		con = connect("viren.db")
		cursor = con.cursor()
		sql = "select * from employee"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + " id " + str(d[0]) + " name " + str(d[1]) + " salary " + str(d[2]) + "\n"
		vw_st_data.insert(INSERT , info)

  
	except Exception as e:
		showerror("Galat Kiya" , e)
	finally :
			
		if con is not None:
			con.close() 	
	


def f3():
	mw.withdraw()
	uw.deiconify()
def f4():
	mw.withdraw()
	dw.deiconify()
def f5():
	aw.withdraw()
	mw.deiconify()
def f6():
	vw.withdraw()
	mw.deiconify()
def f7():
	uw.withdraw()
	mw.deiconify()
def f8():
	dw.withdraw()
	mw.deiconify()
def f9():
	con = None
	try :
		con = connect("viren.db")
		cursor = con.cursor()
		sql = "insert into employee values('%d' ,  '%s' , '%f')"
		id = int(aw_ent_id.get())
		name = aw_ent_name.get()
		salary = float(aw_ent_salary.get())
		cursor.execute(sql % (id , name , salary))
		con.commit()
		showinfo("success" , "record added")
	except Exception as e:
		showerror("Galat Kiya" , e)
	finally :
		aw_ent_id.delete(0 , END)
		aw_ent_name.delete(0 , END)
		aw_ent_salary.delete(0 , END)
		aw_ent_id.focus()
		if con is not None:
			con.close() 	

def f10():
	con = None
	try :
		con = connect("viren.db")
		cursor = con.cursor()
		sql = "update employee set name = '%s' , salary = '%f' where id = '%d'" 
		#sql = "update employee set salary = '%f' where id = '%d'" 
		name = uw_ent_name.get()
		salary = float(uw_ent_salary.get())
		id = int(uw_ent_id.get())
		cursor.execute(sql % (name , salary , id ))
		if cursor.rowcount ==1:
			con.commit()
			showinfo("success" , "record updated")
		else :
			showinfo(id, " does not exists ")
	except Exception as e:
		showerror("Galat Kiya" , e)
		con.rollback()
		print("issue " , e)
	finally:
		if con is not None:
			con.close()

def f11():
	con = None
	try :
		con = connect("viren.db")
		cursor = con.cursor()
		sql = "delete from employee where id = '%d'" 
		id = int(dw_ent_id.get())
		cursor.execute(sql % (id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("record deleted ")
		else :
			showinfo(id, " does not exists ")
	except Exception as e:
		showerror("Galat Kiya" , e)
		con.rollback()
		print("issue " , e)
	finally:
		if con is not None:
			con.close()
	


	

# main window

class BackgroundPage:
	def __init__(self , mw )

mw = Tk()
mw.title("E.M.S")
mw.geometry("600x600+50+50")

#img = PhotoImage(file="try.jpg")
#label = Label( mw, image=img)
#label.place(x=0, y=0)
#img = ImageTk.PhotoImage(Image.open("try.jpg"))
#l=Label(image=img)
#l.pack() 

#image = Image.open("try.jpg")
#photo = ImageTk.PhotoImage(image)

#img_label = Label(image=photo)
#img_label.pack()
 

f = ("Arial" , 30 , "bold")
y = 10

mw_btn_add = Button(mw , text = "Add Employee" , font = f , width = 15 , command = f1)
mw_btn_view = Button(mw , text = "view Employee" , font = f , width = 15 , command = f2)
mw_btn_update = Button(mw , text = "update Employee" , font = f , width = 15 , command = f3)
mw_btn_delete = Button(mw , text = "delete Employee" , font = f , width = 15 , command = f4)
mw_btn_charts = Button(mw , text = "Charts" , font = f , width = 15)


mw_btn_add.pack(pady = y)
mw_btn_view.pack(pady = y)
mw_btn_update.pack(pady = y)
mw_btn_delete.pack(pady = y)
mw_btn_charts.pack(pady = y)


# add window
# add window is a top level on main window


aw = Toplevel(mw)
aw.title("Add Window")
aw.geometry("600x600+50+50")

aw_lab_id = Label(aw , text = "enter id " , font = f)
aw_ent_id = Entry(aw , font = f)

aw_lab_name = Label(aw , text = "enter name " , font = f)
aw_ent_name = Entry(aw , font = f)

aw_lab_salary = Label(aw , text = "enter salary " , font = f)
aw_ent_salary = Entry(aw , font = f)


aw_btn_Save = Button(aw , text = "Save" , font = f , width = 15 , command = f9)
aw_btn_Back = Button(aw , text = "Back" , font = f , width = 15 , command = f5)

aw_lab_id.pack(pady = y)
aw_ent_id.pack(pady = y)
aw_lab_name.pack(pady = y)
aw_ent_name.pack(pady = y)
aw_lab_salary.pack(pady = y)
aw_ent_salary.pack(pady = y)
aw_btn_Save.pack(pady = y)
aw_btn_Back.pack(pady = y)
aw.withdraw()


# VIEW WINDOW

vw = Toplevel(mw)
vw.title("View Window")
vw.geometry("600x600+50+50")

vw_st_data = ScrolledText(vw , width = 40 , height = 25)
vw_btn_back = Button(vw , text = "Back" , font = f , command = f6)
vw_st_data.pack(pady = y)
vw_btn_back.pack(pady = y)
vw.withdraw()



# UPDATE WINDOW

uw = Toplevel(mw)
uw.title("update Window")
uw.geometry("600x600+50+50")

uw_lab_id = Label(uw , text = "enter id " , font = f)
uw_ent_id = Entry(uw , font = f)

uw_lab_name = Label(uw , text = "enter name " , font = f)
uw_ent_name = Entry(uw , font = f)

uw_lab_salary = Label(uw , text = "enter salary " , font = f)
uw_ent_salary = Entry(uw , font = f)


uw_btn_Save = Button(uw , text = "Save" , font = f , width = 15 , command = f10)
uw_btn_Back = Button(uw , text = "Back" , font = f , width = 15 , command = f7)

uw_lab_id.pack(pady = y)
uw_ent_id.pack(pady = y)
uw_lab_name.pack(pady = y)
uw_ent_name.pack(pady = y)
uw_lab_salary.pack(pady = y)
uw_ent_salary.pack(pady = y)
uw_btn_Save.pack(pady = y)
uw_btn_Back.pack(pady = y)
uw.withdraw()






# DELETE WINDOW

dw = Toplevel(mw)
dw.title("delete Window")
dw.geometry("600x600+50+50")

dw_lab_id = Label(dw , text = "enter id " , font = f)
dw_ent_id = Entry(dw , font = f)

dw_btn_Save = Button(dw , text = "Save" , font = f , width = 15 , command = f11)
dw_btn_Back = Button(dw , text = "Back" , font = f , width = 15 , command = f8)

dw_lab_id.pack(pady = y)
dw_ent_id.pack(pady = y)
dw_btn_Save.pack(pady = y)
dw_btn_Back.pack(pady = y)
dw.withdraw()

def confirmExit():
	if askokcancel('Confirm Exit' , 'Do U Really want to exit'):
		mw.destroy()
mw.protocol('WM_DELETE_WINDOW' , confirmExit)




mw.mainloop()
