from tkinter import * 
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
#from PIL import Image, ImageDraw , ImageFont
from PIL import Image, ImageTk
import requests
import matplotlib.pyplot as plt

# *******************************************************

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
		sql = "insert into employee (id , name , salary ) values(?,?,?)"
		sql = "insert into employee values('%d','%s','%f')"
		id = aw_ent_id.get()
		
		sql1="select * from employee"
		cursor.execute(sql1)
		data=cursor.fetchall()

		for d in data:
			if str(d[0])==str(id):
				raise Exception("ID already exists")
		
		 
		
		if id == "" :
			raise Exception(" Please enter ID ")
		if id.isalpha():
			raise Exception("ID shud contain only numbers")



		id1 = int(aw_ent_id.get())

		if id1 == 0:
			raise Exception("ID cannot be null")
		if id1 <= 0 :
			raise Exception(" ID should have only positive integers ")
		
		

				
		name = aw_ent_name.get()

		for char in name :
			if not(("A" <= char and char <= "Z" ) or ("a" <= char and char <= "z" )):
				raise Exception(" Name should contain only alphabets ")
			if (len(name)<2) or (name.isdigit()):
				raise Exception(" Name should contain only alphabets min length 2")	

		if name == "":
			raise Exception(" Please enter name ")

		salary = aw_ent_salary.get()

		if salary == "" :
			raise Exception(" Please enter Salary ")

		if salary.isalpha():
			raise Exception("salary shud contain only numbers")


		salary1 = float(aw_ent_salary.get())

		if salary1 == 0:
			raise Exception("Salary cannot be null")

		if salary1 < 8000 :
			raise Exception(" Salary should be minimum of 8k ")

		if salary1 <= 0 :
			raise Exception(" Salary should have only positive integers ")




		cursor.execute(sql % ( id1 , name , salary1))

#		SELECT COUNT(*) FROM products WHERE employee.id = ?;
#		IF EXISTS (SELECT * FROM Products WHERE id = ?)
#		BEGIN
#		--do what you need if exists

#		cursor.execute(sql % ( id1 , name , salary1))

#		END
#		ELSE
#		BEGIN
#		--do what needs to be done if not
#		showerror("Something went wrong " , e)
#		END


		if cursor.rowcount == 1:
			con.commit()
			showinfo("success" , "record added")
		else :
			showerror("Something went wrong " , e)
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
		sql = "update employee set name = ? , salary = ? where id = ? " 
		sql = "update employee set name = '%s' , salary = '%f' where id = '%d'" 
		

		id = uw_ent_id.get()
		
		 
		
		if id == "" :
			raise Exception(" Please enter ID ")
		if id.isalpha():
			raise Exception("ID shud contain only numbers")



		id1 = int(uw_ent_id.get())

		if id1 == 0:
			raise Exception("ID cannot be null")
		if id1 <= 0 :
			raise Exception(" ID should have only positive integers ")
		

		name = uw_ent_name.get()

		for char in name :
			if not(("A" <= char and char <= "Z" ) or ("a" <= char and char <= "z" )) :
				raise Exception(" Name should contain only alphabets ")
			if (len(name)<2) or (name.isdigit()):
				raise Exception(" Name should contain only alphabets min length 2")	

		if name == "":
			raise Exception(" Please enter name ")

		if not(name.isalpha()):
			raise Exception("name shud contain only letters")

		salary = uw_ent_salary.get()

		if salary == "":
			raise Exception(" Please enter Salary ")

		if salary.isalpha() :
			raise Exception("salary shud contain only numbers")


		salary1 = float(uw_ent_salary.get())

		if salary1 == 0:
			raise Exception("Salary cannot be null")

		if salary1 < 8000:
			raise Exception(" Salary should be minimum of 8k ")

		if salary1 <= 0:
			raise Exception(" Salary should have only positive integers ")


		cursor.execute(sql % ( name , salary1 , id1 ))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("success" , "record updated")
		else :
			showerror("Galat kiya ", " id does not exists ")
	except Exception as e:
		showerror("Galat Kiya" , e)
		con.rollback()
		print("issue " , e)
	finally:
		uw_ent_id.delete(0 , END)
		uw_ent_name.delete(0 , END)
		uw_ent_salary.delete(0 , END)
		uw_ent_id.focus()
		if con is not None:
			con.close()

def f11():
	con = None
	try :
		con = connect("viren.db")
		cursor = con.cursor()
		sql = "delete from employee where id = ? "
		sql = "delete from employee where id = '%d' " 
 
		id = dw_ent_id.get()
		
		 
		
		if id == "" :
			raise Exception(" Please enter ID ")
		if id.isalpha():
			raise Exception("ID shud contain only numbers")



		id1 = int(dw_ent_id.get())

		if id1 == 0 :
			raise Exception("ID cannot be null")
		if id1 <= 0 :
			raise Exception(" ID should have only positive integers ")
		
		cursor.execute(sql % (id1))

		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success" , " record deleted ")
		else :
			showerror(id, " id does not exists ")

	except Exception as e:
		showerror("Galat Kiya" , e)
		con.rollback()
		print("issue " , e)

	finally:
		dw_ent_id.delete(0 , END)
		dw_ent_id.focus()
		if con is not None:
			con.close()


def f12():
	con = None
	try :
		con = connect("viren.db")
		cursor = con.cursor()
		sql = "select name , salary from employee order by salary desc limit 5" 
		cursor.execute(sql)
		data = cursor.fetchall()
		name = []
		salary = []	
		for d in data :
			name.append(d[0])
			salary.append(d[1])

		plt.bar(name , salary , color = ["red"] , width = 0.5)

		plt.xlabel("Name")
		plt.ylabel("Salary")
		plt.title("Salary of Top 5 Employees")
		plt.show()

	except Exception as e:
		showerror("Galat Kiya" , e)
		
	finally:
		if con is not None:
			con.close()

	

# **************************************************************	

# main window

mw = Tk()
mw.title("E.M.S")
mw.geometry("1600x850+0+0")
mw.state("zoomed")






main_image = Image.open("ems1.jpg")
photo_main = ImageTk.PhotoImage(main_image)


main_image = Label(mw , image=photo_main)
main_image.place(x = 1 , y = 1)





#temp_image = Image.open("weather.png")
#photo_temp = ImageTk.PhotoImage(temp_image)


#temp_image = Label(mw , image=photo_temp)
#temp_image.place(x = 0 , y = 600)


mycanvas = Canvas(main_image , width = 1600 , height = 850)
mycanvas.pack(fill = "both" , expand = True)

mycanvas.create_image(0,0,anchor=NW,image=photo_main)



#text = Text(mw , width = 40 , height = 10 , wrap = WORD)
#text.insert(END , ' WELCOME TO MY APPLICTION')
#text.place(x = 300 , y = 100)

f = ("Arial" , 25 , "bold")
y = 10

mw_btn_add = Button(main_image , text = "Add Employee" , font = f , width = 15 , command = f1 )
mw_btn_view = Button(main_image , text = "View Employee" , font = f , width = 15 , command = f2)
mw_btn_update = Button(main_image , text = "Update Employee" , font = f , width = 15 , command = f3)
mw_btn_delete = Button(main_image ,  text = "Delete Employee" , font = f , width = 15 , command = f4)
mw_btn_charts = Button(main_image , text = "Charts" , font = f , width = 15 , command = f12)


mw_btn_add.place(x = 100 , y = 100)
mw_btn_view.place(x = 100 , y = 200)
mw_btn_update.place(x = 100 , y = 300)
mw_btn_delete.place(x = 100 , y = 400)
mw_btn_charts.place(x = 100 , y = 500)




try :
	wa = "https://ipinfo.io"
	res = requests.get(wa)
	data = res.json()
	city = data["city"]
	state = data["region"]
	
	loc = data["loc"]
	latlong = loc.split(",")
	lat = latlong[0]
	lng = latlong[1]


	a1 = "https://api.openweathermap.org/data/2.5/weather"
	a2 = "?q=" + city
	a3 = "&appid=" + "696f758d0711d9b25f219e59ea85da38"
	a4 = "&units=" + "metric"
	wa = a1 + a2 +a3 + a4
	res = requests.get(wa)
   #	print(res)
	data = res.json()
	# print(data)

	temp = data["main"]["temp"]
	

except Exception as e:
	print("issue ",e)

text_canvas4 = mycanvas.create_text(300,700)
mycanvas.itemconfig(text_canvas4 , text="Location  = " , font = f , fill = "white")


#current_loc = Label(img_label , text = "Location = " , font = f)
#current_loc.place(x = 100 , y = 700)

text_canvas5 = mycanvas.create_text(900,700)
mycanvas.itemconfig(text_canvas5 , text="Temperature  = " , font = f , fill = "white")

#current_temp = Label(img_label , text = "Temp = " , font = f)
#current_temp.place(x = 700 , y = 700)

text_canvas6 = mycanvas.create_text(480,700)
mycanvas.itemconfig(text_canvas6 , text= city , font = f , fill = "white")

#T1 = Text(main_image, height = 1, width = 9 , font = f)
#T2 = Text(main_image, height = 1, width = 7 , font = f)

text_canvas7 = mycanvas.create_text(1100,700)
mycanvas.itemconfig(text_canvas7 , text= temp , font = f , fill = "white")

#T1.place(x = 420 , y = 680)
#T2.place(x = 1100 , y = 680)

#T1.insert(END , city)
#T2.insert(END , temp)


# ************************************************************


# add window
# add window is a top level on main window


aw = Toplevel(mw)
aw.title("Add Window")
aw.geometry("1600x850+0+0")
aw.state("zoomed")


add_image = Image.open("add.jpg")
photo_add = ImageTk.PhotoImage(add_image)

add_img = Label(aw , image=photo_add)
add_img.place(x = 1 , y = 1)

 

mycanvas = Canvas(add_img , width = 1600 , height = 850)
mycanvas.pack(fill = "both" , expand = True)

mycanvas.create_image(0,0,anchor=NW,image=photo_add)

text_canvas = mycanvas.create_text(200,120)
mycanvas.itemconfig(text_canvas , text="Enter ID" , font = f , fill = "white")



#aw_lab_id = Label(add_img , text = "enter id " ,  width = 10 , font = f )
aw_ent_id = Entry(add_img , font = f)
#aw_lab_id.wm_attributes('-transparentcolor' , 'brown')


text_canvas2 = mycanvas.create_text(200,220)
mycanvas.itemconfig(text_canvas2 , text="Enter Name" , font = f , fill = "white")


#aw_lab_name = Label(add_img , text = "enter name " , width = 10  , font = f)
aw_ent_name = Entry(add_img , font = f)

text_canvas3 = mycanvas.create_text(200,320)
mycanvas.itemconfig(text_canvas3 , text="Enter Salary" , font = f , fill = "white")

#aw_lab_salary = Label(add_img , text = "enter salary " , width = 10  , font = f)
aw_ent_salary = Entry(add_img , font = f)


aw_btn_Save = Button(add_img , text = "Save" , font = f , width = 15 , command = f9)
aw_btn_Back = Button(add_img , text = "Back" , font = f , width = 15 , command = f5)

#aw_lab_id.place(x = 100 , y = 100)
aw_ent_id.place(x = 400 , y = 100)
#aw_lab_name.place(x = 100 , y = 200)
aw_ent_name.place(x = 400 , y = 200)
#aw_lab_salary.place(x = 100 , y = 300)
aw_ent_salary.place(x = 400 , y = 300)
aw_btn_Save.place(x = 100 , y = 600)
aw_btn_Back.place(x = 100 , y = 700)
aw.withdraw()


# ************************************************************************


# VIEW WINDOW

vw = Toplevel(mw)
vw.title("View Window")
vw.geometry("1600x850+0+0")

view_image = Image.open("view1.jpg")
photo_view = ImageTk.PhotoImage(view_image)

img_view = Label(vw , image=photo_view)
img_view.place(x = 1 , y = 1) 




vw_st_data = ScrolledText(img_view , width = 52 , height = 33)
vw_btn_back = Button(img_view , text = "Back" , font = f ,width = 20 , command = f6)
vw_st_data.place(x = 140 , y = 90)
vw_btn_back.place(x = 210 , y = 670)
vw.withdraw()


# ************************************************************************


# UPDATE WINDOW

uw = Toplevel(mw)
uw.title("update Window")
uw.geometry("1600x850+0+0")

update_image = Image.open("uw1.jpg")
photo_update = ImageTk.PhotoImage(update_image)

img_update = Label(uw , image=photo_update)
img_update.place(x = 1 , y = 1)


mycanvas = Canvas(img_update , width = 1600 , height = 850)
mycanvas.pack(fill = "both" , expand = True)

mycanvas.create_image(0,0,anchor=NW,image=photo_update)

text_canvas = mycanvas.create_text(200,90)
mycanvas.itemconfig(text_canvas , text="Enter ID" , font = f , fill = "white")


 

#uw_lab_id = Label(img_update , text = "enter id " ,width = 15 , font = f)
uw_ent_id = Entry(img_update , width = 20 ,font = f)


text_canvas = mycanvas.create_text(220,240)
mycanvas.itemconfig(text_canvas , text="Enter updated Name" , font = f , fill = "white")


#uw_lab_name = Label(img_update , text = "enter name " , width = 15 ,font = f)
uw_ent_name = Entry(img_update ,width = 20 , font = f)


text_canvas = mycanvas.create_text(220,420)
mycanvas.itemconfig(text_canvas , text="Enter updated Salary" , font = f , fill = "white")


#uw_lab_salary = Label(img_update , text = "enter salary " ,width = 15 , font = f)
uw_ent_salary = Entry(img_update , width = 20 , font = f)


uw_btn_Save = Button(img_update , text = "Save" , font = f , width = 15 , command = f10)
uw_btn_Back = Button(img_update , text = "Back" , font = f , width = 15 , command = f7)

#uw_lab_id.place(x = 90 , y = 60)
uw_ent_id.place(x = 580 , y = 60)
#uw_lab_name.place(x = 90 , y = 200)
uw_ent_name.place(x = 580 , y = 220)
#uw_lab_salary.place(x = 90 , y = 400)
uw_ent_salary.place(x = 580 , y = 400)
uw_btn_Save.place(x = 100 , y = 650)
uw_btn_Back.place(x = 600 , y = 650)
uw.withdraw()





# ************************************************************************



# DELETE WINDOW

dw = Toplevel(mw)
dw.title("delete Window")
dw.geometry("1600x850+0+0")

delete_image = Image.open("delete2.png")
photo_delete = ImageTk.PhotoImage(delete_image)

img_delete = Label(dw , image=photo_delete)
img_delete.place(x = 1 , y = 1)
 

mycanvas = Canvas(img_delete , width = 1600 , height = 850)
mycanvas.pack(fill = "both" , expand = True)

mycanvas.create_image(0,0,anchor=NW,image=photo_delete)

text_canvas6 = mycanvas.create_text(730,190)
mycanvas.itemconfig(text_canvas6 , text="Enter ID" , font = f , fill = "white")


#dw_lab_id = Label(img_delete , text = "Enter id " , width = 15 , font = f)
dw_ent_id = Entry(img_delete ,width = 30 , font = f)

dw_btn_Save = Button(dw , text = "Delete" , font = f , width = 12 , command = f11)
dw_btn_Back = Button(dw , text = "Back" , font = f , width = 12 , command = f8)

#dw_lab_id.place(x = 650 , y = 190)
dw_ent_id.place(x = 520 , y = 280)
dw_btn_Save.place(x = 550 , y = 700)
dw_btn_Back.place(x = 850 , y = 700)
dw.withdraw()

def confirmExit():
	if askokcancel('Confirm Exit' , 'Do U Really want to exit'):
		mw.destroy()
mw.protocol('WM_DELETE_WINDOW' , confirmExit)

def confirmExit():
	if askokcancel('Confirm Exit' , 'Do U Really want to exit'):
		aw.destroy()
aw.protocol('WM_DELETE_WINDOW' , confirmExit)

def confirmExit():
	if askokcancel('Confirm Exit' , 'Do U Really want to exit'):
		uw.destroy()
uw.protocol('WM_DELETE_WINDOW' , confirmExit)

def confirmExit():
	if askokcancel('Confirm Exit' , 'Do U Really want to exit'):
		dw.destroy()
dw.protocol('WM_DELETE_WINDOW' , confirmExit)




mw.mainloop()
