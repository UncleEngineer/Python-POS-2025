from tkinter import *
from tkinter import ttk, messagebox
import os
from basicsql import *
from elements import SalesTab, ProductTab

# PATH = os.getcwd()
# print(PATH)
# p1 = os.path.join(PATH,'tab1.png')

GUI = Tk()
w = 1000
h = 600

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()

x = (ws/2)-(w/2)
y = (hs/2)-(h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')
# GUI.geometry('700x600')
GUI.title('โปรแกรมขายของร้านลุง')

##########MENU###########
menubar = Menu(GUI)
GUI.config(menu=menubar)

#File Menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='เปิดเมนูเพิ่มสินค้า',command=lambda: print('Add Product'))
filemenu.add_command(label='ออกจากโปรแกรม',command=lambda: GUI.quit())

#About Menu

def AboutMenu(event=None):
    GUI2 = Toplevel()
    w = 500
    h = 300
    
    ws = GUI.winfo_screenwidth()
    hs = GUI.winfo_screenheight()
    
    x = (ws/2)-(w/2)
    y = (hs/2)-(h/2)
    
    GUI2.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')
    
    uncle_icon = PhotoImage(file='uncle.png').subsample(2) # .subsample(2) resize down / 2
    Label(GUI2,image=uncle_icon).pack()
    
    Label(GUI2,text='โปรแกรมนี้เป็นโปรแกรมสำหรับขายของ\nคุณสามารถใช้งานได้ฟรี ไม่มีค่าใช้จ่าย\nTel: 0812345678').pack()
    
    GUI2.mainloop()


aboutmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='About',menu=aboutmenu)
aboutmenu.add_command(label='เกี่ยวกับโปรแกรม',command=AboutMenu)

GUI.bind('<F12>',AboutMenu)

##########TAB###########
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

# สร้าง Frame สำหรับแต่ละแท็บ
T1 = Frame(Tab)
T2 = Frame(Tab)

# โหลดไอคอนแท็บ
tab_icon1 = PhotoImage(file='tab1.png')
tab_icon2 = PhotoImage(file='tab2.png')

# เพิ่มแท็บ
Tab.add(T1,text='เมนูขาย',image=tab_icon1,compound='left')
Tab.add(T2,text='เพิ่มสินค้า',image=tab_icon2,compound='left')

# สร้าง instance ของแต่ละแท็บ
sales_tab = SalesTab(T1)

product_tab = ProductTab(T2, sales_tab)  # ส่ง sales_tab เพื่อให้อัปเดตปุ่มได้

GUI.mainloop()