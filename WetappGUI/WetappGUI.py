import tkinter as tk
from tkinter import ttk
import random 
import datetime
import re
import sys
import time
from PIL import Image,ImageTk

class Dog():
    def __init__ (self,name_owner=" ",surname_owner=" ",pesel_owner=[0], number_dog=0, name_dog=" ", race_dog=" ", age_dog=0, date_dog=""):
        self.name_owner=name_owner
        self.surname_owner=surname_owner
        self.pesel_owner=pesel_owner
        self.number_dog=number_dog
        self.name_dog=name_dog
        self.race_dog=race_dog
        self.age_dog=age_dog
        self.date_dog=date_dog

    def tab_read(self):
        return [self.name_owner,self.surname_owner,self.pesel_owner, self.name_dog, self.race_dog, self.age_dog]

    def __str__ (self):
        return "Imie opiekuna:"+self.name_owner+"\nNazwisko opiekuna:"+self.surname_owner+"\nPesel opiekuna:"+self.pesel_owner+"\nNumer psa:"+self.number_dog+"\nNazwa psa:"+self.name_dog+"\nRasa psa:"+self.race_dog+"\nWiek psa:"+self.age_dog+"\nData dodana:"+str(self.date_dog)
    
    def remove(self,number):
        if self.number_dog==number: 
            del self 
            print("usuniety")

    def __del__(self):
        print("Object deleted")
            

def draw_number(tab):  
    while True:
        tab2=[]
        for i in range(0,6):
            tab2.append(random.randint(0,9))
        tab2="".join([str(elm) for elm in tab2])
        if tab2 in [tab[number].number_dog for number, x in enumerate(tab)]:
            continue
        break
    return tab2

def check_data_dog(name_owner,surname_owner,pesel_owner,name_dog,race_dog,age_dog):
    global wrong
    if 'wrong' not in globals():
        wrong=tk.Label(frame, text=" ")
    wrong.destroy()
    if name_owner!="":
        if surname_owner!="":
            if len(pesel_owner)==11 and  pesel_owner.isdigit():
                if name_dog!="":
                    if race_dog!="":
                        if age_dog.isdigit():
                            return True
                        else:
                            wrong=tk.Label(frame, text="Wrong age of dog!",fg="green", bg="Black", padx=5 ,pady=2, font=("MV Boli",))
                            wrong.grid(row=7, column=3)
                            return False
                    else:
                        wrong=tk.Label(frame, text="Wrong race of dog!",fg="green", bg="Black", padx=5 ,pady=2, font=("MV Boli",))
                        wrong.grid(row=6, column=3)
                        return False
                else:
                    wrong=tk.Label(frame, text="Wrong name of dog!",fg="green", bg="Black", padx=5 ,pady=2, font=("MV Boli",))
                    wrong.grid(row=5, column=3)
                    return False
            else:
                wrong=tk.Label(frame, text="Wrong Pesel of owner!",fg="green", bg="Black", padx=5 ,pady=2, font=("MV Boli",))
                wrong.grid(row=4, column=3)
                return False
        else:
            wrong=tk.Label(frame, text="Wrong surname of owner!",fg="green", bg="Black", padx=5 ,pady=2, font=("MV Boli",))
            wrong.grid(row=3, column=3)
            return False
    else:
        wrong=tk.Label(frame, text="Wrong name of owner!",fg="green", bg="Black", padx=5 ,pady=2, font=("MV Boli",))
        wrong.grid(row=2, column=3)
        return False
def add_dog_menu():
    for widgets in frame.winfo_children():
        widgets.destroy()

    name_owner_var=tk.StringVar()
    surname_owner_var=tk.StringVar()
    pesel_owner_var=tk.StringVar()
    name_dog_var=tk.StringVar()
    race_dog_var=tk.StringVar()
    age_dog_var=tk.StringVar()

    paragraph=tk.Label(frame, text=" ",pady=23,fg="white", bg="Black", font=("MV Boli",)).grid(row=1, column=1)
    title=tk.Label(frame, text="add dog",pady=23,fg="white", bg="Black", font=("MV Boli",30)).grid(row=1, column=2)
    paragraph2=tk.Label(frame, text=" ",padx=90,fg="white", bg="Black", font=("MV Boli",)).grid(row=1, column=3)
    T1=["name of owner","surname of owner","pesel of owner","name of dog","race of dog","age of dog",]
    Var1=[name_owner_var,surname_owner_var,pesel_owner_var,name_dog_var,race_dog_var,age_dog_var]
    for i in range(len(Var1)):
        tk.Label(frame, text=T1[i],fg="white", bg="Black", padx=5 ,pady=2, font=("MV Boli",)).grid(row=i+2, column=1)
        tk.Entry(frame, textvariable=Var1[i]).grid(row=i+2, column=2)

    B1=tk.Button(frame, text="create",padx=20, command=lambda: add_dog(name_owner_var,surname_owner_var,pesel_owner_var,name_dog_var,race_dog_var,age_dog_var)).grid(row=8, column=1)
    B2=tk.Button(frame, text="Back",padx=20, command=lambda: Create_Menu(frame)).grid(row=8, column=2)
    return frame
def add_dog(name_owner_var,surname_owner_var,pesel_owner_var,name_dog_var,race_dog_var,age_dog_var):
    name_owner=name_owner_var.get()
    surname_owner=surname_owner_var.get()
    pesel_owner=pesel_owner_var.get()
    number_dog=draw_number(tab)
    name_dog=name_dog_var.get()
    race_dog=race_dog_var.get()
    age_dog=age_dog_var.get()
    date_dog=datetime.date.today()

    correctness=check_data_dog(name_owner,surname_owner,pesel_owner,name_dog,race_dog,age_dog)
    
    if correctness==True:
        tab.append(Dog(name_owner,surname_owner,pesel_owner,number_dog,name_dog,race_dog,age_dog,date_dog))
        newWindow = tk.Toplevel(frame)
        newWindow.title("New dog")
        newWindow.iconbitmap('images/Dog_Footprint.ico')
        newWindow.geometry("200x200")
        newWindow.grab_set()
        l1=tk.Label(newWindow, text=tab[len(tab)-1]).grid(row=1,column=1)
        B1=tk.Button(newWindow, text="Quit", command=lambda: Create_Menu(frame)).grid(row=2, column=1)
        del name_owner_var, surname_owner_var ,pesel_owner_var, name_dog_var, race_dog_var, age_dog_var, name_owner, surname_owner ,pesel_owner, name_dog, race_dog, age_dog, number_dog,date_dog

def browse_dogs():
    i="low"
    for widgets in frame.winfo_children():
        widgets.destroy()
    style=ttk.Style()
    style.theme_use('classic')
    #style.configure('Vertical.TScrollbar',background='blue',bordercolor="red", arrowcolor="white") XD nie wiem jak to zrobic
    style.configure("Treeview",background='black', foreground='green',rowheight=25,fieldbackground="black")
    style.configure('Treeview.Heading', background='black', foreground='green')
    style.map('Treeview', background=[('selected','green')],foreground=[('selected','black')])
    columns=('name_owner', 'surname_owner', 'pesel_owner','number_dog', 'name_dog', 'race_dog','age_dog')
    tree_scroll=tk.Scrollbar(frame,orient='vertical')
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    tree=ttk.Treeview(frame, yscrollcommand=tree_scroll.set, selectmode="browse", column=columns, show='headings', height=5)
    tree_scroll.config(command=tree.yview)
    for x in columns: tree.column(x,width=100)
    tree.heading('name_owner', text='Name Owner', anchor=tk.CENTER, command=lambda: segregation(tree, 0, "high",0))
    tree.heading('surname_owner', text='Surname Owner', anchor=tk.CENTER, command=lambda: segregation(tree, 1, "high",0))
    tree.heading('pesel_owner', text='Pesel Owner', anchor=tk.CENTER, command=lambda: segregation(tree, 2, "high",0))
    tree.heading('number_dog', text='Number Dog', anchor=tk.CENTER, command=lambda: segregation(tree, 3,"high",0))
    tree.heading('name_dog', text='Name Dog', anchor=tk.CENTER, command=lambda: segregation(tree, 4, "high",0))
    tree.heading('race_dog', text='Race Dog', anchor=tk.CENTER, command=lambda: segregation(tree, 5, "high",0))
    tree.heading('age_dog', text='Age Dog', anchor=tk.CENTER, command=lambda: segregation(tree, 6, "high",0))
    tk.Button(frame, text="add", command=lambda: print("x"), padx=20).pack()
    tk.Button(frame, text="search", command=lambda: print("x"), padx=20).pack()
    tk.Button(frame, text="deleate", command=lambda: remove_browsed_dog(tree,tab), padx=20).pack()
    tk.Button(frame, text="back", command=lambda: Create_Menu(frame), padx=20).pack()
    for number,x in enumerate(tab):
        tree.insert(parent='',index=number,iid=x.number_dog ,values=(x.name_owner, x.surname_owner, x.pesel_owner, x.number_dog, x.name_dog, x.race_dog, x.age_dog))
        #tree.insert(parent=number, index=tk.END ,text="xxxxxxxxxxxxx")
    tree.pack()

def remove_browsed_dog(tree,tab):
    x=tree.selection()[0]
    tree.delete(x)
    for k in tab: k.remove(x)
    for x in tab:
        #print(x)
        print("-----------")
    return tab

def segregation(tree2, y, i,l):
    for x in tree2.get_children():
        if ((tree2.index(x)+1)==len(tree2.get_children()) and l==0): return segregation(tree2, y, "low",0)
        if (tree2.index(x)+1)==len(tree2.get_children()): return tree2
        num1=tree2.item(x)['values']
        num2=tree2.item(tree2.next(x))['values']
        if num1 is str:
            if ((int(num1[y]) > int(num2[y]) and i=="high") or (int(num1[y]) < int(num2[y]) and i=="low")):
                tree2.move(x,tree2.parent(x),tree2.index(x)+1)
                return segregation(tree2, y, i, 1)
        else:
            if ((str(num1[y]) > str(num2[y]) and i=="high") or (str(num1[y]) < str(num2[y]) and i=="low")):
                tree2.move(x,tree2.parent(x),tree2.index(x)+1)
                return segregation(tree2, y, i, 1)

def look_for_dog_menu():
    for widgets in frame.winfo_children():
        widgets.destroy()
    look_for_number_var=tk.StringVar()
    title=tk.Label(frame, text="look for dog",pady=23,fg="white", bg="Black", font=("MV Boli",30)).grid(row=1, column=1,columnspan = 2)
    tk.Label(frame, text="number of dog",fg="white", bg="Black", padx=5 ,pady=2, font=("MV Boli",)).grid(row=2, column=1)
    look_for_number_enter=tk.Entry(frame, textvariable=look_for_number_var).grid(row=2, column=2)
    tk.Button(frame, text="search", command=lambda: look_for_dog(look_for_number_var), padx=20).grid(row=3, column=1)
    tk.Button(frame, text="Back", command=lambda: Create_Menu(frame), padx=20).grid(row=3, column=2)
    return frame

def look_for_dog(look_for_number_var):
    look_for_number=look_for_number_var.get()
    newWindow = tk.Toplevel(frame)
    newWindow.title("Found dog")
    newWindow.iconbitmap('images/Dog_Footprint.ico')
    newWindow.geometry("300x100")
    newWindow_label = tk.Label(newWindow, image=bg2)
    newWindow_label.pack()
    newWindow_label.place(x=0, y=0, relwidth=1, relheight=1)
    newWindow.grab_set()
    if look_for_number in [tab[number].number_dog for number, x in enumerate(tab)] and len(look_for_number)==6 and look_for_number.isdigit():
        tk.Label(newWindow, text=[tab[number] for number,x in enumerate(tab) if look_for_number==tab[number].number_dog]).grid(row=1,column=1)
        tk.Button(newWindow, text="Quit", command=newWindow.destroy).grid(row=2, column=1)
    else:
        tk.Label(newWindow, text="Wrong number's dog").grid(row=1,column=1)
        tk.Button(newWindow, text="Quit", command=newWindow.destroy).grid(row=2, column=1)

def edit_dog_menu():
    for widgets in frame.winfo_children():
        widgets.destroy()

    edit_dog_var=tk.StringVar()
    title=tk.Label(frame, text="edit dog",pady=23,fg="white", bg="Black", font=("MV Boli",30)).grid(row=1, column=1,columnspan = 2)
    edit_dog_number=tk.Label(frame, text="number of dog",fg="white", bg="Black", padx=5 ,pady=2, font=("MV Boli",)).grid(row=2, column=1)
    edit_dog_number_enter=tk.Entry(frame, textvariable=edit_dog_var).grid(row=2, column=2)
    B1=tk.Button(frame, text="Search", command=lambda: edit_dog(edit_dog_var), padx=20).grid(row=3, column=1)
    B2=tk.Button(frame, text="Back", command=lambda: Create_Menu(frame), padx=20).grid(row=3, column=2)

def edit_dog(edit_dog_var):
    edit_dog=edit_dog_var.get()
    number_edit=None
    for number, x in enumerate(tab):
        if edit_dog==tab[number].number_dog: number_edit=number
    if number_edit is None:
        newWindow = tk.Toplevel(frame)
        newWindow.title("Wrong number")
        newWindow.iconbitmap('images/Dog_Footprint.ico')
        newWindow.geometry("300x100")
        newWindow_label = tk.Label(newWindow, image=bg2)
        newWindow_label.pack()
        newWindow_label.place(x=0, y=0, relwidth=1, relheight=1)
        newWindow.grab_set()
        l=tk.Label(newWindow, text="Wrong number's dog").grid(row=1,column=1)
        B=tk.Button(newWindow, text="Quit", command=newWindow.destroy).grid(row=2, column=1)
    else: 
        for widgets in frame.winfo_children():
            widgets.destroy()
        name_owner_var=tk.StringVar()
        surname_owner_var=tk.StringVar()
        pesel_owner_var=tk.StringVar()
        name_dog_var=tk.StringVar()
        race_dog_var=tk.StringVar()
        age_dog_var=tk.StringVar()

        paragraph=tk.Label(frame, text=" ",pady=23,fg="white", bg="Black", font=("MV Boli",)).grid(row=1, column=1)
        title=tk.Label(frame, text="edit dog",pady=23,fg="white", bg="Black", font=("MV Boli",30)).grid(row=1, column=2)
        paragraph2=tk.Label(frame, text=" ",padx=90,fg="white", bg="Black", font=("MV Boli",)).grid(row=1, column=3)

        T1=["name of owner","surname of owner","pesel of owner","name of dog","race of dog","age of dog",]
        Var1=[name_owner_var,surname_owner_var,pesel_owner_var,name_dog_var,race_dog_var,age_dog_var]

        for i in range(len(Var1)):
            tk.Label(frame, text=T1[i],fg="white", bg="Black", padx=5 ,pady=2, font=("MV Boli",)).grid(row=i+2, column=1)
            Var2=tk.Entry(frame, textvariable=Var1[i])
            Var2.grid(row=i+2, column=2)
            Var2.insert(0,tab[number_edit].tab_read()[i])

        B1=tk.Button(frame, text="create",padx=20, command=lambda: edit_dog_save(name_owner_var,surname_owner_var,pesel_owner_var,name_dog_var,race_dog_var,age_dog_var,number_edit)).grid(row=8, column=1)
        B2=tk.Button(frame, text="Back",padx=20, command=lambda: Create_Menu(frame)).grid(row=8, column=2)

def edit_dog_save(name_owner_var,surname_owner_var,pesel_owner_var,name_dog_var,race_dog_var,age_dog_var,number):
    name_owner=name_owner_var.get()
    surname_owner=surname_owner_var.get()
    pesel_owner=pesel_owner_var.get()
    number_dog=tab[number].number_dog
    name_dog=name_dog_var.get()
    race_dog=race_dog_var.get()
    age_dog=age_dog_var.get()
    date_dog=tab[number].date_dog

    correctness=check_data_dog(name_owner,surname_owner,pesel_owner,name_dog,race_dog,age_dog)

    if correctness==True:
        tab[number]=Dog(name_owner,surname_owner,pesel_owner, number_dog, name_dog, race_dog, age_dog, date_dog)
        newWindow = tk.Toplevel(frame)
        newWindow.title("Edited dog")
        newWindow.iconbitmap('images/Dog_Footprint.ico')
        newWindow.geometry("200x200")
        newWindow.grab_set()
        l1=tk.Label(newWindow, text=tab[number]).grid(row=1,column=1)
        B1=tk.Button(newWindow, text="Quit", command=lambda: Create_Menu(frame)).grid(row=2, column=1)
        del name_owner_var, surname_owner_var ,pesel_owner_var, name_dog_var, race_dog_var, age_dog_var, name_owner, surname_owner ,pesel_owner, name_dog, race_dog, age_dog, number_dog,date_dog

def remove_dog_menu():
    for widgets in frame.winfo_children():
        widgets.destroy()

    remove_number_var=tk.StringVar()
    title=tk.Label(frame, text="remove dog",pady=23,fg="white", bg="Black", font=("MV Boli",30)).grid(row=1, column=1,columnspan = 2)
    remove_number=tk.Label(frame, text="number of dog",fg="white", bg="Black", padx=5 ,pady=2, font=("MV Boli",)).grid(row=2, column=1)
    remove_number_enter=tk.Entry(frame, textvariable=remove_number_var).grid(row=2, column=2)
    B1=tk.Button(frame, text="Del", command=lambda: remove_dog(remove_number_var), padx=20).grid(row=3, column=1)
    B2=tk.Button(frame, text="Back", command=lambda: Create_Menu(frame), padx=20).grid(row=3, column=2)
    return frame

def remove_dog(remove_number_var):
    remove_number=remove_number_var.get()
    newWindow = tk.Toplevel(frame)
    newWindow.title("Deleted")
    newWindow.iconbitmap('images/Dog_Footprint.ico')
    newWindow.geometry("300x100")
    newWindow_label = tk.Label(newWindow, image=bg2)
    newWindow_label.pack()
    newWindow_label.place(x=0, y=0, relwidth=1, relheight=1)
    newWindow.grab_set()
    if remove_number in [tab[number].number_dog for number, x in enumerate(tab)] and len(remove_number)==6 and remove_number.isdigit():
        for number,x in enumerate(tab):
            if tab[number].number_dog == remove_number:
                del tab[number]
        l=tk.Label(newWindow, text="Dog has been deleted").grid(row=1,column=1)
        B=tk.Button(newWindow, text="Quit", command=newWindow.destroy).grid(row=2, column=1)

    else:
        l=tk.Label(newWindow, text="Wrong number's dog").grid(row=1,column=1)
        B=tk.Button(newWindow, text="Quit", command=newWindow.destroy).grid(row=2, column=1)

def retrieve_dog_number_menu():
    for widgets in frame.winfo_children():
        widgets.destroy()
    retrieve_pesel_number_var=tk.StringVar()
    retrieve_name_owner_var=tk.StringVar()
    retrieve_surname_owner_var=tk.StringVar()
    T1=["pesel number","name owner","surname owner"]
    Var1=[retrieve_pesel_number_var,retrieve_name_owner_var,retrieve_surname_owner_var]
    title=tk.Label(frame, text="retrieve dog number",pady=23,fg="white", bg="Black", font=("MV Boli",30)).grid(row=1, column=1,columnspan = 2)
    for i in range(len(Var1)):
        tk.Label(frame, text=T1[i],fg="white", bg="Black", padx=5 ,pady=2, font=("MV Boli",)).grid(row=i+2, column=1)
        tk.Entry(frame, textvariable=Var1[1]).grid(row=i+2, column=2)

    B1=tk.Button(frame, text="Retrieve", command=lambda: retrieve_dog_number(retrieve_pesel_number_var,retrieve_name_owner_var,retrieve_surname_owner_var), padx=20).grid(row=5, column=1)
    B2=tk.Button(frame, text="Back", command=lambda: Create_Menu(frame), padx=20).grid(row=5, column=2)

def retrieve_dog_number(retrieve_pesel_number_var,retrieve_name_owner_var,retrieve_surname_owner_var):
    retrieve_pesel_number=retrieve_pesel_number_var.get()
    retrieve_name_owner=retrieve_name_owner_var.get()
    retrieve_surname_owner=retrieve_surname_owner_var.get()
    newWindow = tk.Toplevel(frame)
    newWindow.title("Recovered")
    newWindow.iconbitmap('images/Dog_Footprint.ico')
    newWindow.geometry("300x100")
    newWindow_label = tk.Label(newWindow, image=bg2)
    newWindow_label.pack()
    newWindow_label.place(x=0, y=0, relwidth=1, relheight=1)
    newWindow.grab_set()
    wanted_number=None
    wanted_number=[tab[number].number_dog+" "+tab[number].name_dog for number, x in enumerate(tab) if retrieve_pesel_number==tab[number].pesel_owner and retrieve_name_owner==tab[number].name_owner and retrieve_surname_owner==tab[number].surname_owner]
    if wanted_number is not None:
        l=tk.Label(newWindow, text="Dog number "+", ".join(wanted_number)).grid(row=1,column=1)
        B=tk.Button(newWindow, text="Quit", command=newWindow.destroy).grid(row=2, column=1)
    else:
        l=tk.Label(newWindow, text="Wrong data").grid(row=1,column=1)
        B=tk.Button(newWindow, text="Quit", command=newWindow.destroy).grid(row=2, column=1)

def close_program():
        newWindow = tk.Toplevel(frame)
        newWindow.title("Close")
        newWindow.iconbitmap('images/Dog_Footprint.ico')
        newWindow.geometry("300x100")
        newWindow_label = tk.Label(newWindow, image=bg2)
        newWindow_label.pack()
        newWindow_label.place(x=0, y=0, relwidth=1, relheight=1)
        l=tk.Label(newWindow, text="Would you like to save the changes?").grid(row=1,column=1,columnspan = 3)
        B1=tk.Button(newWindow, text="Yes", command=save_data).grid(row=2, column=1)
        B2=tk.Button(newWindow, text="No", command=root.destroy).grid(row=2, column=2)
        B3=tk.Button(newWindow, text="Cancel", command=newWindow.destroy).grid(row=2, column=3)

def save_data():
    with open("BazaDanych.txt","w") as plik:
        for number, x in enumerate(tab):
            plik.writelines(str(tab[number])+"\n/\n")
    root.destroy()

def Create_Menu(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()
        #pady=80,padx=80
    frame.pack()
    l=tk.Label(frame, text="Menu",pady=23,fg="white", bg="Black", font=("MV Boli", 30))
    l.grid(row=1, column=1)
    B1=Menu_Buttons(frame)
    return frame

def Menu_Buttons(frame):
    F1=[add_dog_menu,browse_dogs,look_for_dog_menu,edit_dog_menu,remove_dog_menu,retrieve_dog_number_menu,close_program]
    B1_texts=["add dog","browse dogs","look for dog","edit dog","remove dog","retrieve dog number","close program"]
    B1=[tk.Button(frame, text=B1_text) for B1_text in B1_texts]
    for i in range(len(B1)):
        B1[i].grid(row=i+2, column=1, padx=5 ,pady=2)
        B1[i]["command"]=F1[i]
    return B1

def load_dogs():
    tab=[]
    tabc=[]
    y=""
    with open("BazaDanych.txt", "r") as plik:
        while True:
            x=plik.read(1)
            if x==":":
                while True:
                    x=plik.read(1)
                    if x=="\n":
                        break
                    y=y+x
                tab.append(y)
                y=""
            if x=="/":
                tabc.append(Dog(tab[0],tab[1],tab[2],tab[3],tab[4],tab[5],tab[6],tab[7]))
                tab=[]
            elif x=="":
                break

    del tab, y
    return tabc

def root_function():
    root=tk.Tk()
    root.iconbitmap('images/Dog_Track.ico')
    root.title("WetApp")
    root.geometry("500x500")
    root.minsize(width=500, height=500)
    root.configure(background="black")
    bg2=ImageTk.PhotoImage(Image.open("images/Background2.png"))
    image2=Image.open("images/Background1.png")
    bg1=ImageTk.PhotoImage(image2)
    copy_of_bg = image2.copy()
    return root, bg2,copy_of_bg,bg1
def resize_l(event):
    new_width = event.width
    new_height = event.height
    image_copy = copy_of_bg.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image_copy)
    background1.config(image = photo)
    background1.image = photo 
def Event_Time(ic):
    image_copy = ic.resize((root.winfo_width(),root.winfo_height()))
    photo = ImageTk.PhotoImage(image_copy)
    background1.config(image = photo)
    background1.image = photo 
def Anim_Background():
    l=tk.Label(root)
    l.after(4000,lambda: Event_Time(bg1b))
    l.after(4300,lambda: Event_Time(bg1bb))
    l.after(4600,lambda: Event_Time(copy_of_bg))
    l.after(4800,Anim_Background)

if __name__== "__main__":
    tab=load_dogs()
    root,bg2,copy_of_bg,bg1=root_function()
    bg1b=Image.open("images/Background1b.png")
    bg1bb=Image.open("images/Background1bb.png")
    background1 = tk.Label(root, image = bg1)
    background1.pack()
    n=0
    background1.place(relwidth=1, relheight=1)
    background1.bind('<Configure>', resize_l)
    Anim_Background()
    frame=tk.Frame(root, bg="black")
    frame=Create_Menu(frame)
    root.mainloop()
