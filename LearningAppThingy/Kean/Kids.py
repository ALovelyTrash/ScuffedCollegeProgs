import tkinter as tk
from tkinter import messagebox as mb

# Header Frame
def Frame_1(WH,Y):
    tops = tk.Frame(kean,width=WH[0],height=WH[1])
    tops.place(y=Y)
    cv = tk.Canvas(tops,width=WH[0],height=WH[0])
    cv.place(x=0,y=0)
    img = tk.PhotoImage(file=f'./img/{content[0]}.gif')
    cv.image = img
    cv.create_image(0,0,anchor='nw',image=img)

    menbar = tk.Menu(kean,bg=ui)
    opts = tk.Menu(menbar,bg=ui)
    rand = tk.Menu(menbar,bg=ui)

    for i in range(3):
        opts.add_command(label=options[i],command=cmds[i])

    rand.add_command(label='Say Hello',command=lambda:mb.showinfo('Hello','Hello My Friend'))
    menbar.add_cascade(label='Options',menu=opts)
    menbar.add_cascade(label='Random',menu=rand)
    kean.config(menu=menbar)

# Footer Frame
def Frame_2(WH,Y):
    bottoms = tk.Frame(kean,width=WH[0],height=WH[1])
    bottoms.place(x=0,y=Y)
    cv = tk.Canvas(bottoms,width=WH[0],height=WH[1])
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

    for i in range(3):
    	tk.Button(left,text=str(options[i]),bg=ui,command=cmds[i],width='10',height='3').place(x=50,y=(i*100))



# Content Frame
def Frame_4():
    global right
    right = tk.Frame(kean,width=wh[0],height=wh[1])
    right.place(x=xy[0],y=xy[1])

    cv = tk.Canvas(right,width=wh[0],height=wh[1],bg=ui)
    cv.pack()
    img = tk.PhotoImage(file='./img/cont.gif')
    cv.image = img
    cv.create_image(0,0,anchor='nw',image=img)


def Shape():
    for win in right.winfo_children():
        win.destroy()

    # Main COntent Frame
    newRight = tk.Frame(kean,bg=ui,width=wh[0],height=wh[1])
    newRight.place(x=xy[0],y=xy[1])

    tk.Button(newRight,text='BACK',bg=ui,command=lambda:[newRight.destroy(),Frame_4()]).pack(side='top')

    def Topsies(arg,wh):
        pop = tk.Toplevel(kean,width=wh[0],height=wh[1])
        canvas = tk.Canvas(pop,width=wh[0],height=wh[1])
        canvas.place(x=0,y=0)
        img = tk.PhotoImage(file=f'./img/{arg}.gif')
        canvas.image = img
        canvas.create_image(0,0,anchor='nw',image=img)

    # Shape Command Poop
    def Press(event):
        thing = canvas.find_withtag('current')[0]

        if thing == square:
            Topsies('square',(400,400))
        elif thing == circle:
            Topsies('circle',(400,400))
        elif thing == triangle:
            Topsies('triangle',(400,400))
        elif thing == rectangle:
            Topsies('rectangle',(400,400))


    # Layer Frame
    canvas = tk.Canvas(newRight,width=wh[0],height=int(wh[1])-30,bg=ui)
    canvas.pack()

    # Shapes according to XY1 to XY2
    square = canvas.create_rectangle(20,20,140,140,outline='black',fill='red')
    circle = canvas.create_oval(190,20,310,140,outline='black',fill='yellow')
    dots = [80,150,140,250,140,250,20,250]
    triangle = canvas.create_polygon(dots,outline='black',fill='green')
    rectangle = canvas.create_rectangle(190,150,340,250,outline='black',fill='blue')


    # Bind Stuff from shapes
    canvas.tag_bind(square, '<ButtonPress-1>',Press)
    canvas.tag_bind(circle, '<ButtonPress-1>',Press)
    canvas.tag_bind(triangle, '<ButtonPress-1>',Press)
    canvas.tag_bind(rectangle, '<ButtonPress-1>',Press)

def About():
    for win in right.winfo_children():
        win.destroy()
    Frame_4()

    Abt = tk.Toplevel(kean,width=640,height=640)
    cv = tk.Canvas(Abt,width=640,height=640)
    cv.place(x=0,y=0)

    img = tk.PhotoImage(file='./img/about us.gif')
    cv.image = img
    cv.create_image(0,0,anchor='nw',image=img)

    with open('./img/about_us.txt','r') as lol:
        final = lol.read()
    cv.create_text(200,300,text=final,font='Verdana 20',fill='Blue')

def Exit():
	kean.destroy()



# Root Window
kean = tk.Tk()
kean.geometry('600x500')

ui = 'orange'

cmds = (Shape,About,Exit)

options = ('shapes','about Me','exit')
content = ('head','foot','menu','content')

# Headers, Footers, Menubar
Frame_1(('600','100'),'0')
Frame_2(('600','100'),'400')

# Menus/Selection
Frame_3(('600','300'),'100')


# Actual Context
shapes = ('square','circle','triangle')
wh = ('400','300')
xy = ('200','100')
Frame_4()


# End
kean.mainloop()
