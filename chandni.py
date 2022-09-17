from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *


mw = Tk()
mw.title("E.M.S.")
mw.geometry("600x600+50+50")

f = ("Arial", 30, "bold")
y = 15
mw_btn_add = Button(mw, text="Add", font = f , width = 15)
mw_btn_view = Button(mw, text="View", font = f , width = 15)
mw_btn_update = Button(mw, text="Update", font = f , width = 15)
mw_btn_delete = Button(mw, text="Delete", font = f , width = 15)
mw_btn_add.pack(pady=y)
mw_btn_view.pack(pady=y)
mw_btn_update.pack(pady=y)
mw_btn_delete.pack(pady=y)



aw = Toplevel(mw)
aw.title("Add Employee ")
aw.geometry("600x600+50+50")
aw_lab_id = Label(aw, text = "enter id ", font =f )
aw_ent_id = Entry(aw, font=f )
aw_lab_name = Label(aw, text = "enter name ", font =f )
aw_ent_name = Entry(aw, font=f )
aw_lab_salary = Label(aw, text = "enter salary ", font =f )
aw_ent_salary = Entry(aw, font=f )
aw_btn_save = Button(aw, text = "Save", font =f)
aw_btn_back = Button(aw, text= "Back", font=f)
aw_lab_id.pack(pady=y)
aw_ent_id.pack(pady=y)
aw_lab_name.pack(pady=y)
aw_ent_name.pack(pady=y)
aw_lab_salary.pack(pady=y)
aw_ent_salary.pack(pady=y)
aw_btn_save.pack(pady=y)
aw_btn_back.pack(pady=y)


vw = Toplevel(mw)
vw.title("View Employee ")
vw.geometry("600x600+50+50")
vw_st_data = ScrolledText(vw, width=20, height=10, font =f)
vw_btn_back = Button(vw, text="Back", font =f)
vw_st_data.pack(pady=y)
vw_btn_back.pack(pady=y)







mw.mainloop()