import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
import numpy as np
import pytesseract
import os
import sys
from datetime import datetime
import tkinter.font as font
from tkinter import filedialog
from tkinter import messagebox
from helpsec import open_hs
 
root = tk.Tk()
 
root.title("Picxt: Find Images by Keyword")
root.geometry('449x525')
root_bg = "#0F0730"
root['background']=root_bg # #080614 !! #1f0830
root.resizable(False, False)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon_path = "main_icon2.ico"
icon = Image.open(resource_path(icon_path))
resized_icon = icon.resize((32, 32), Image.LANCZOS)
icon_photo = ImageTk.PhotoImage(resized_icon)
root.iconphoto(True, icon_photo)


sfi= ImageTk.PhotoImage(Image.open(resource_path("SF1.png")).resize((160, 41), Image.LANCZOS))               
sci = ImageTk.PhotoImage(Image.open(resource_path("SC1.png")).resize((160, 41), Image.LANCZOS))
cri = ImageTk.PhotoImage(Image.open(resource_path("CR1.png")).resize((160, 41), Image.LANCZOS))
hpi = ImageTk.PhotoImage(Image.open(resource_path("HP1.png")).resize((130, 41), Image.LANCZOS))
eti = ImageTk.PhotoImage(Image.open(resource_path("EX1.png")).resize((130, 41), Image.LANCZOS))




header_main_img = resource_path("header_png.png")
hdr_img = Image.open(header_main_img)
hdr_rsz_img = hdr_img.resize((277, 111), Image.LANCZOS)
hdr_img_fin = ImageTk.PhotoImage(hdr_rsz_img)



header = tk.Label(root, bg=root_bg, bd=0)
header.grid(column = 0, row = 0, columnspan=2, pady=(0, 10), sticky="Ew")
header.config(image=hdr_img_fin)
header.image = hdr_img_fin

ent_lbl = tk.Label(root, font=("Poppins", 12), text="Enter your keyword below : ",
                foreground="#b5b5b5", background=root_bg) 
ent_lbl.grid(column=0, row=2, columnspan=2, padx=26, sticky="W")

txt_entry = tk.Entry(root, width=35, font=('Arial 14'), bd=0,  background="#271559", 
            foreground="white", insertbackground="white")
txt_entry.grid(column =0, row =3, columnspan=2, padx=20, pady=(5, 20), ipady=5)




def selectFolder():
    global file_path
    file_path = filedialog.askdirectory()
    if file_path:
        check_png_path = resource_path("green_chk.png")
        image = Image.open(check_png_path)
        resized_image = image.resize((50, 50), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)

        gtick_lbl.config(image=tk_image)
        gtick_lbl.image = tk_image  

gtick_lbl = tk.Label(root, bg=root_bg, bd=0) #"#150736"
gtick_lbl.grid(column=1, row=1, sticky="W", pady=(15, 30))

pytesseract.pytesseract.tesseract_cmd = resource_path("pytess-assets/tesseract.exe")

def searching_lbl_fn():
    global searching_lbl
    searching_lbl = tk.Label(root, font=("Poppins semibold", 12), text="Searching, Please wait for a moment...", 
                          foreground="#b5b5b5", background=root_bg)
    searching_lbl.grid(column=0, row=6, columnspan=2, padx=25, pady=15, sticky="EW")


find = []
flag_lb_contains = False


image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')

def search(): 
    try:
        file_path
    except NameError:
        messagebox.showerror("Error", "Please Select A Folder Before Continuing")
        return
    if (flag_lb_contains == True):
        find.clear()
    global count
    count = 0
    global keyword
    keyword = txt_entry.get()
    if not keyword:
        messagebox.showerror("Error", "Please Enter Keyword Before Continuing")
        return
    searching_lbl_fn()
    root.update()
    try:
        for filename in os.listdir(file_path):
            f = os.path.join(file_path, filename)
            if f.lower().endswith(image_extensions):
                img = np.array(Image.open(f))
                text = pytesseract.image_to_string(img)
                if os.path.isfile(f):
                    if keyword in text:
                        find.append(f)
                        count = count + 1 
    
    except Image.UnidentifiedImageError:
        # messagebox.showerror("Error", "There was an error while \n scanning one or more images")
        pass
    except FileNotFoundError:
        searching_lbl.destroy()
        messagebox.showerror("Error", "An error occured because \n the folder or files inside it no longer exist")
    except PermissionError:
        searching_lbl.destroy()
        messagebox.showinfo("Permission Denied", "Make sure you are authorized to access the directory")
        return
    except Exception as e:
        searching_lbl.destroy()
        messagebox.showerror("Error", "An error occured while scanning")
        return
    searching_lbl.destroy()            
    show_message_box()
    

def clear():
    txt_entry.delete(0, 'end')

buttonFont = font.Font(family='Product Sans', size=12)

selFold_bt = tk.Button(root, image=sfi, bg=root_bg, activebackground=root_bg,
                    bd=0, width=163, height=43, command=selectFolder,)
selFold_bt.grid(column=0, row=1,  
             padx=(26, 0), pady=(20, 30), sticky="W")


search_bt = tk.Button(root, image=sci, bg=root_bg, activebackground=root_bg,
                    bd=0, width=163, height=43, command=search)
search_bt.grid(column=0, row=4, padx=30, pady=(15, 23), sticky="W")

clear_bt = tk.Button(root, image=cri, bg=root_bg, activebackground=root_bg,
                    bd=0, width=163, height=43, command=clear)
clear_bt.grid(column=1, row=4, padx=(30, 29), pady=(15, 23), sticky="E")

help_bt = tk.Button(root, image=hpi, bg=root_bg, activebackground=root_bg,
                    bd=0, width=132, height=43,command=open_hs)
help_bt.grid(column=0, row=5, padx=30, pady=15, sticky="W")

exit_bt = tk.Button(root, image=eti, bg=root_bg, activebackground=root_bg,
                    bd=0, width=132, height=43, command=root.destroy)
exit_bt.grid(column=1, row=5, padx=30, pady=15, sticky="E")



def open_image(event):
    
        selected_item = listbox.focus()
        if selected_item:
            try:
                selected_file_path = listbox.item(selected_item, "values")[0]
                cleaned_file_path = selected_file_path.replace("\ ", " ")
                abs_file_path = os.path.abspath(cleaned_file_path)
                os.startfile(abs_file_path)
            except FileNotFoundError:
                messagebox.showerror("Error: Unable to locate the file", "File could not be opened because \n it may have been modified or moved \n or it no longer exists")
            
            except IndexError:
                messagebox.showerror("An Error Occured", "Error opening the file")
            
            except OSError:
                messagebox.showerror("An Error Occured", "Error opening the file, \n try after some time")
    


def show_message_box():
    global final_count
    if count == 0:
        result = "No match found!"
        response = messagebox.showinfo("Search Results", result)
        
    elif count == 1:
        final_count = (str)(count) + " Result "
        result =  "1 match found! \nDo you want to see the results?"
        response = messagebox.askquestion("Search Results", 
                                      result)
    elif count > 1:
        final_count = (str)(count) + " Results "
        result = (str)(count) + " matches found! \nDo you want to see the results?"
        response = messagebox.askquestion("Search Results", 
                                      result)
    
    if response == 'yes':
        show_result_window()


def show_result_window():
    result_window = tk.Toplevel(root)
    result_window.title("List of files found")
    result_window['background']="#2c2f30"

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",rowheight=25, foreground="#e8e8e8", background="#141414", 
                    fieldbackground="#e8e8e8", font=("Poppins", 11))
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
    style.configure("Treeview.Heading", font=("Poppins bold", 11), background="orange",
                    foreground="white", borderwidth=0, padding=(3, 0))

    style.map("Treeview.Heading", background=[("active", "#f5d925")], foreground=[("active", "#1e2021")])


    global flag_lb_contains
    global listbox
    listbox = ttk.Treeview(result_window)
    listbox["columns"] = ("path","Date Created", "Type", "Size")
    
    listbox.heading("#0", text="Name", anchor="w")
    listbox.heading("path", text="path", anchor="w")
    listbox.heading("Date Created", text="Date Created", anchor="w")
    listbox.heading("Type", text="Type", anchor="w")
    listbox.heading("Size", text="Size", anchor="w")
    listbox.column("#0", width=450, minwidth=350)
    listbox.column("Date Created", width=170, minwidth=155)
    listbox.column("Type", width=140, minwidth=115, stretch=False)
    listbox.column("Size", width=140, minwidth=125, stretch=False)
    listbox.configure(displaycolumns=("Date Created", "Type", "Size"))

    fin_cnt_lbl = tk.Label(result_window, text = final_count + "Found for " + '"' + keyword + '"', 
                        font=("Poppins semibold", 12), background="#2c2f30", foreground="#e8e8e8")
    fin_cnt_lbl.pack(side="top", fill="both", pady=2)

    

    for index, i in enumerate(find):
        f_mtime = getCreationDate(i)
        f_extn = getType(i)
        f_size = getSize(i)
        tags = ("even_row") if index % 2 == 0 else ("odd_row")
        
        listbox.insert("", "end", text=os.path.basename(i), tags=tags, values=([i], f_mtime , f_extn, f_size))
    
    flag_lb_contains = True
    listbox.pack(side="left", fill="both", expand=True, padx=14, pady=(1, 14))
    listbox.bind("<Double-Button-1>", open_image)

    listbox.tag_configure("even_row", background="#3d3d3d")
    listbox.tag_configure("odd_row", background="#2e2e2e")

    vsb = ttk.Scrollbar(listbox, orient="vertical", command=listbox.yview)
    listbox.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right", fill="both")
    listbox.propagate(False)

    
    


def getCreationDate(found_file):
    try:
        return datetime.fromtimestamp(os.path.getmtime(found_file)).strftime("%d-%b-%y %H:%M")
    except FileNotFoundError:
        return "Error!"
    except ValueError:
        return "Error!"
    except Exception:
        return "Error!"

def getType(found_file):
    try:
        return os.path.splitext(found_file)[1]
    except FileNotFoundError:
        return "Error!"
    except Exception:
        return "Error!"

def getSize(found_file):
    try:
        return format_file_size(os.path.getsize(found_file))
    except FileNotFoundError:
        return "Error!"
    except Exception:
        return "Error!"


def format_file_size(size):
    if size < 0:
        raise ValueError("File size cannot be negative")
        
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} GB"



root.mainloop()
