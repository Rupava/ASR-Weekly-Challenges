import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog,Text,Label,Button,PhotoImage
from collections import Counter
from selenium import webdriver
import os

url = "https://coolors.co/"
colors = []
hex_list = []
hex_color = []
color_names = []
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

root = tk.Tk()
root.title("Colors For You")
root.resizable(0,0)

canvas = tk.Canvas(root,height=350,width=670,bg="#555555")
canvas.pack()
frame = tk.Canvas(root, height = 750,width = 750, bg = "#CCCCCC")
frame.place(relwidth = 0.9,relheight=0.9,relx=0.05,rely=0.05)

global color_view
color_view = tk.Canvas(frame, height = 95,width = 95, bg = "#5BEB60")
color_view.place(relx=0.05,rely=0.45)

label_path = Label(frame, text= 'No Image Selected')
label_path.place(relx=0.16,rely=0.038)

list_colors = Listbox(frame)
list_colors.place(width = 200 ,relx=0.65,rely=0.25)


def selectImage():
    clearData()
    global img
    root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select Image",filetypes = (("png files","*.png"),("jpg files","*.jpg")))
    if root.filename != '':
        label_path.config(text = root.filename)
        image = Image.open(root.filename)
        image = image.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        label_image = Label(frame,image=img)    
        label_image.place(relx=0.3,rely=0.17)
        

def getColors():
    if root.filename != '':
        got_img = Image.open(root.filename)
        size = w,h = got_img.size
        data = got_img.load()

        for x in range (w):
            for y in range (h):
                color = data[x,y]
                hex_color = (''.join([hex(c)[2:].rjust(2,'0') for c in color]))
                colors.append(hex_color)

        color_count = (Counter(colors))
        hex_list = (list(color_count.keys()))
        
        for item in hex_list: 
            list_colors.insert(END,item)
    colors.clear()
    color_names.clear()
    hex_list.clear()

def view_color():
    get_string = list_colors.get(ANCHOR)
    anchor_color ='#' + get_string[0:6]
    color_view.config(bg=anchor_color)


def getColorNames():
    list_colors.delete(0,'end')
    if root.filename != '':
        got_img = Image.open(root.filename)
        size = w,h = got_img.size
        data = got_img.load()

        for x in range (w):
            for y in range (h):
                color = data[x,y]
                hex_color = (''.join([hex(c)[2:].rjust(2,'0') for c in color]))
                colors.append(hex_color)

        color_count = (Counter(colors))
        hex_list = (list(color_count.keys()))

        for x in range(len(hex_list)):
                driver.get(url + hex_list[x])
                color_names.append(driver.find_element_by_id("color-picker-page_preview_name").text)   



        print('________________________________')
        print('Your colors- ')
        for x in range(len(color_names)): 
            var_result = hex_list[x] +': '+ color_names[x]
            list_colors.insert(END,var_result)
            print(var_result)
        print('________________________________')



def clearData():
    colors.clear()
    color_names.clear()
    hex_list.clear()
    list_colors.delete(0,'end')


bt_path = Button(frame,text="Add Image",command = selectImage)
bt_path.place(relx=0.025,rely=0.035)

bt_gcolor = Button(frame,text="Get Colors",command = getColors)
bt_gcolor.place(relx=0.025,rely=0.14)

bt_gcolor = Button(frame,text="Get Color Names",command = getColorNames)
bt_gcolor.place(relx=0.025,rely=0.25)

bt_clear = Button(frame,text="Clear",command = clearData)
bt_clear.place(relx=0.16,rely=0.14)

bt_clear = Button(frame,text="View",command = view_color)
bt_clear.place(relx=0.22,rely=0.25)


root.mainloop()