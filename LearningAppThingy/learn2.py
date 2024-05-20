import tkinter as tk
from tkinter import messagebox as mb
from random import randint as rt

class Menu(tk.Frame):

    def __init__(self,arg,bg,wh,xy):
        super().__init__(arg)
        self.place(x=xy[0],y=xy[1],width=wh[0],height=wh[1])

        self.file = tk.PhotoImage(file=f'./assets/{bg}')
        tk.Label (self,image=self.file).place(x=0,y=0)

    def Btns(self,subs,bg,wh,padxy):

        for x in range(4):
            tk.Button (self,
                text=subs[x],command=Op[x],bg=bg,relief='flat',
                width=wh[0],height=wh[1]) \
            .grid(row=x,column=1,padx=padxy[0],pady=padxy[1])

def Op_1():
    for widg in Content.winfo_children():
        widg.destroy()
    ContCall(Root,bg=ContImg[4],wh=contres[0],xy=contres[1])
    Content.Color(wh=(15,5),padxy=(20,20),cl=0)
    Content.Color(wh=(15,5),padxy=(20,20),cl=2)
    Content.Back()

def Op_2():
    for widg in Content.winfo_children():
        widg.destroy()
    ContCall(Root,bg=ContImg[5],wh=contres[0],xy=contres[1])
    Content.Math()
    Content.Back()

def Op_3(bg=6,wh=(640,640),xy=(0,0)):
    About = tk.Toplevel(Root,width=wh[0],height=wh[1])
    canvas = tk.Canvas(About,width=wh[0],height=wh[1])
    canvas.place(x=0,y=0)
    file = tk.PhotoImage(file=f'./assets/{ContImg[bg]}')
    canvas.image = file
    canvas.create_image(xy[0],xy[1],anchor='nw',image=file)

    if bg == 6:
        with open('./assets/about_us.txt', 'r') as f:
            output = f.read()
        canvas.create_text(200,300,text=output,font='Verdana 20',fill='DeepPink')

def Op_4():
    scan = mb.askyesno('Exit','Ya Sure ya want to exit mate?')
    if scan:
        Root.destroy()

Op = (Op_1,Op_2,Op_3,Op_4)



class Cont(tk.Frame):

    def __init__(self,arg,bg,wh,xy):
        super().__init__(arg)

        self.file = tk.PhotoImage(file=f'./assets/{bg}')
        tk.Label (self,image=self.file).place(x=0,y=0)

        self.place(x=xy[0],y=xy[1],width=wh[0],height=wh[1])

    def Color(self,wh,padxy,cl):
        for x in range(2):
            tk.Button(self,command=lambda x=x: Op_3(bg=(x+cl+7),wh=(300,300)),
                       bg=var[x+cl],relief='flat',width=wh[0],height=wh[1]) \
                    .grid(row=x,column=cl,padx=padxy[0],pady=padxy[1])

    def Math(self):
        a = rt(0,9)
        b = rt(0,9)

        def ans():
            if self.entry.get() == str(a+b):
                mb.showinfo('Correct!',
                            f'Correct Answer!\nThe answer is {a+b}')
            elif self.entry.get() == "":
                mb.showwarning('Huh?', 'Its Blank!')
            else:
                mb.showerror('Incorrect!',
                             f'Incorrect Answer!\nIts not {self.entry.get()}')

        tk.Label(self,text=f'{a} + {b} = ?\nWhats Yer Answer\n Kid?',
                 font='Verdana 25').pack(pady='30')
        self.entry = tk.Entry(self, width='20',font='Verdana 20',bg=ui)
        self.entry.pack()

        tk.Button(self,text='Next',relief='flat',bg=ui,command=ans) \
                .pack(side='right')


    def Back(self):
        def BackCreate():
            for widg in self.winfo_children():
                widg.destroy()
            ContCall(Root,bg=ContImg[3],wh=contres[0],xy=contres[1])

        tk.Button(self,text='BACK',relief='flat',bg=ui,command=BackCreate) \
                .place(x=10,y=260)



class HeadFoot(tk.Frame):

    def __init__(self,arg,bg,wh,xy):
        super().__init__(arg)

        self.file = tk.PhotoImage(file=f'./assets/{bg}')
        tk.Label (self,image=self.file).grid(row=0,column=0)

        self.place(x=xy[0],y=xy[1],width=wh[0],height=wh[1])

    def Nav(self,bg):

        menubar = tk.Menu(Root)
        menubar.config(bg=bg)
        opt = tk.Menu(menubar, bg=bg)
        inf = tk.Menu(menubar, bg=bg)
        stt = tk.Menu(menubar, bg=bg)

        for i in range(4):
            opt.add_command(label=subs[i], command=Op[i])

        inf.add_command(label='About Us', command=Op[2])
        stt.add_command(label='Change UI')

        menubar.add_cascade(label='Options',menu=opt)
        menubar.add_cascade(label='Info',menu=inf)
        menubar.add_cascade(label='Settings',menu=stt)
        Root.config(menu=menubar)


def ContCall(main,bg,wh,xy):
    global Content
    Content = Cont(main,bg=bg,wh=wh,xy=xy)


Root = tk.Tk()

# UI
ui = 'pink'

Root.geometry ('600x500')
Root.protocol('WM_DELETE_WINDOW',Op_4)
Root.config(bg=ui)

# THE CONTENTS - RESOLUTION os (WIDTHxHEIGHT) and (X & Y)
contres = (('350','300'),('250','100'))
ContImg = ('head.gif','foot.gif','menu.gif','cont.gif',
            'color.gif','math.gif','about_us.gif',
           'red.gif','orange.gif','yellow.gif','green.gif')

# CALLING OF CONTENTS
ContCall(Root,bg=ContImg[3],wh=contres[0],xy=contres[1])
var = ('red','orange','yellow','green')



# THE MENU, padxy = PADX & PADY
subs = ('Colors','Math','About Us','Exit')
Menu(Root,bg=ContImg[2],wh=('250','300'),xy=('0','100')) \
        .Btns(subs,bg=ui,wh=(10,2),padxy=(70,10))



# HEADERS AND FOOTERS, wh = (WIDTHxHEIGHT), xy = (X & Y)
Head = HeadFoot(Root,bg=ContImg[0],wh=('600','100'),xy=('0','0')).Nav(bg=ui)
Foot = HeadFoot(Root,bg=ContImg[1],wh=('600','100'),xy=('0','400'))

Root.mainloop()
