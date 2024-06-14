import tkinter as tk


# Header Frame
def Frame_1(WH,Y):
    tops = tk.Frame(kean,width=WH[0],height=WH[1])
    tops.place(y=Y)
    cv = tk.Canvas(tops,width=WH[0],height=WH[0])
    cv.place(x=0,y=0)
    img = tk.PhotoImage(file=f'./img/{content[0]}.gif')
    cv.image = img
    cv.create_image(0,0,anchor='nw',image=img)

    menbar = tk.Menu(kean)
    options = tk.Menu(menbar)
    options.add_command(label='hallo')
    menbar.add_cascade(label='Options',menu=options)
    kean.config(menu=menbar)

# Footer Frame
def Frame_2(WH,Y):
    bottoms = tk.Frame(kean,width=WH[0],height=WH[1])
    bottoms.place(y=Y)
    cv = tk.Canvas(bottoms,width=900,height=900)
    cv.place(x=0,y=0)

    img = tk.PhotoImage(file=f'./img/{content[1]}.gif')
    cv.image = img
    cv.create_image(0,0,anchor='nw',image=img)

# Menu Frame
def Frame_3(WH,Y):
    global left
    left = tk.Frame(kean,width=WH[0],height = WH[1])
    left.place(y=Y)
    cv = tk.Canvas(left,width=WH[0],height=WH[1])
    #cv.place(x=0,y=0)
    cv.pack()
    img = tk.PhotoImage(file=f'./img/{content[2]}.gif')
    cv.image = img
    cv.create_image(0,0,anchor='nw',image=img)
    
    #tk.Label(left,image=img).place(x=0,y=0)

    for i in range(0,3):
    	tk.Button(left,text=str(options[i]),command=cmds[i]).place(x=50,y=(i*50))



# Content Frame
def Frame_4():

	global right
	right = tk.Frame(kean,width=wh[0],height=wh[1])
	right.place(x=xy[0],y=xy[1])
	tk.Label(right,text='jxhsbd',bg='green').place(x=0,y=0)


def Shape():
	for win in right.winfo_children():
		win.destroy()
	newRight = tk.Frame(kean,width=wh[0],height=wh[1])
	newRight.place(x=xy[0],y=xy[1])
	#tk.Button(newRight,text='hsjdhs').pack(
	square = tk.PhotoImage(file=f'./img/{shapes[0]}.gif')
	circle = tk.PhotoImage(file=f'./img/{shapes[1]}.gif')
	triangle = tk.PhotoImage(file=f'./img/{shapes[2]}.gif')
		
	op_shapes = (square,circle,triangle)
	for i in range(3):
		tk.Button(newRight,image=op_shapes[i]).place(x=20,y=i*:50)

def About():
	for win in right.winfo_children():
		win.destroy()

	Abt = tk.Toplevel(kean,width=200,height=200)
	cv = tk.Canvas(Abt,width=200,height=200)
	cv.place(x=0,y=0)

	img = tk.PhotoImage(file='./img/about.gif')
	cv.image = img
	cv.create_image(0,0,anchor='nw',image=img)

def Exit():
	kean.destroy()



# Root Window
kean = tk.Tk()
kean.geometry('1300x800')

cmds = (Shape,About,Exit)

options = ('shapes','about Me','exit')
content = ('head','foot','menu','content')

# Headers, Footers, Menubar
Frame_1(('1300','100'),'0')
Frame_2(('1300','100'),'700')

# Menus/Selection
Frame_3(('300','500'),'100')


# Actual Context
shapes = ('square','circle','triangle')
wh = ('1000','500')
xy = ('300','100')
Frame_4()


# End
kean.mainloop()
